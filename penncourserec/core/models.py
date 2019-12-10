from django.db import models


class Course(models.Model):
    name = models.TextField()
    code = models.TextField()
    courseRating = models.DecimalField(max_digits=2, decimal_places=1)
    profRating = models.DecimalField(max_digits=2, decimal_places=1)
    difficulty = models.DecimalField(max_digits=2, decimal_places=1)
    selected = models.BooleanField(default=False)
