from django.db import models

# Single model that encapsulates all courses in the recommender.
class Course(models.Model):
    name = models.TextField(max_length=50)
    code = models.TextField(max_length=10)
    description = models.TextField(default="")
    courseRating = models.DecimalField(max_digits=2, decimal_places=1)
    profRating = models.DecimalField(max_digits=2, decimal_places=1)
    difficulty = models.DecimalField(max_digits=2, decimal_places=1)
    selected = models.BooleanField(default=False)

    def as_dict(self):
        return {'name': self.name, 'code': self.code, 'description': self.description, 'courseRating': self.courseRating, 'profRating': self.profRating, 'difficulty': self.difficulty, 'selected': self.selected}

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.code)
