from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrollment_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
