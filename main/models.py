from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    date      = models.DateTimeField(default=timezone.now)
    head = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.CharField(max_length=200, default=True)

    comment   = models.TextField()

    
    
    def __str__(self):
        return f'{self.project_name} Project'

    def get_absolute_url(self):
    	return reverse('proj-content', kwargs = {'pk':self.pk})



class Task(models.Model):
	member_name = models.CharField(max_length=100)
	task = models.TextField(max_length=200)

	def __str__(self):
		return f'{self.member_name} Task'

	