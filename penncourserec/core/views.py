from django.shortcuts import render
from core.models import Course
import json


def splash(request):
    return render(request, 'splash.html', {})


def select(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        course_name = request.POST['name']
        for course in courses:
            if course.name == course_name:
                course.selected = not course.selected
    names = [course.name for course in courses]
    js_names = json.dumps(names)
    return render(request, 'bubbles.html', {'courses': js_names})


def recommend(request):
    return render(request, 'recommend.html', {})
