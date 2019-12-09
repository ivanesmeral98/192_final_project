from django.shortcuts import render
from core.models import Course


def splash(request):
    return render(request, 'splash.html', {})


def select(request):
    courses = Course.objects.all()
    return render(request, 'bubbles.html', {'courses': courses})


def recommend(request):
    return render(request, 'recommend.html', {})
