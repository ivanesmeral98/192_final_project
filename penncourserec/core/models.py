from django.db import models


class Course(models.Model):
    name = models.TextField()
    code = models.TextField()
    courseRating = models.IntegerField(default=0)
    profRating = models.IntegerField(default=0)
    difficulty = models.IntegerField(default=0)
    selected = models.BooleanField
