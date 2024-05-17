from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)

    class Meta:
        ordering = ['-roll_no']

    def __str__(self):
        return f"{self.first_name}---{self.roll_no}"

