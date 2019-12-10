from django.shortcuts import render
from core.models import Course
import json
from pymagnitude import *
from sklearn.neighbors import NearestNeighbors


def splash(request):
    return render(request, 'splash.html', {})


def select(request):
    courses = Course.objects.all()

    if request.POST:
        course_name = request.POST.get('name', None)
        selected_course = Course.objects.get(name=course_name)
        selected_course.selected = not selected_course.selected
        selected_course.save()
    else:
        for course in courses:
            course.selected = False
            course.save()
    names = [course.name for course in courses]
    js_names = json.dumps(names)
    return render(request, 'bubbles.html', {'courses': js_names})


def recommend(request):
    elmo = Magnitude("elmo-light-1536D.magnitude")
    knn = NearestNeighbors()
    X_train = []
    X_train_dict = {}
    X_test = []
    for course in Course.objects.all():
        all_text = course.name + course.code + course.description
        if course.selected:
            X_test.append(np.append(elmo.query(all_text), [float(course.courseRating), float(course.profRating), float(course.difficulty)]))
        else:
            embedding = np.append(elmo.query(all_text), [float(course.courseRating), float(course.profRating), float(course.difficulty)])
            X_train_dict[course.name] = embedding
            X_train.append(embedding)

    X_train = np.array(X_train)
    X_test = np.array(X_test)
    X_test = np.sum(X_test, axis=0)
    knn.fit(X_train)
    recommendations = set()

    nearest = knn.kneighbors(X_test.reshape(1, -1), 3)[1][0]
    for idx in nearest:
        for k in X_train_dict:
            if np.array_equal(X_train_dict[k], X_train[idx]):
                recommendations.add(k)
                break

    rec_queries = Course.objects.filter(name__in=recommendations)

    return render(request, 'recommend.html', {"recs": rec_queries})


def course(request):
    course_to_view = Course.objects.get(code=request.GET['code'])
    return render(request, 'course.html', {'course': course_to_view})