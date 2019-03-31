from django import forms
from .models import Task
class ProductForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = [
		 	'task',
		 	'member_name',
		 	
		]


