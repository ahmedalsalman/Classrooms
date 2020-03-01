from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	subject = models.CharField(max_length=120)
	grade = models.IntegerField()
	year = models.IntegerField()
	teacher = models.ForeignKey(User, null = True, blank = True ,on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
    name = models.CharField(max_length = 120)
    dob = models.DateField()
    genderChoices = [
    	('M', "Male"),
    	('F', "Female"),
    ]

    gender = models.CharField(max_length = 50,choices=genderChoices,default='m')
    exam_grade = models.IntegerField()
    classroom = models.ForeignKey(Classroom, null = True, blank = True, on_delete =models.CASCADE)
