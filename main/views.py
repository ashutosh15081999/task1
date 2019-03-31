from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Task
from django.contrib import messages
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
from .views import *
from django.contrib.auth.models import User
from .forms  import ProductForm
def home(request):
    context = {
        'project': Project.objects.all(),
    }
    return render(request, 'main/home.html', context)


# def book(request):
# 	listofbooks={
# 		'libooks':Book.objects.all(),
# 	}
# 	return render(request,'bookstore/book.html',listofbooks)

class PostListView(LoginRequiredMixin,ListView):
	model = Project
	template_name = 'main/project.html'
	context_object_name = 'liprojects'
	ordering = ['-date']

	def form_valid(self,form):
		form.instance.head = self.request.user
		return super().form_valid(form)


#<app>/<model>_<viewtype.html>

class PostDetailView(DetailView):
	model = Project
	template_name = 'main/select_project.html'
	#context_object_name = 'libooks'

class PostCreateView(LoginRequiredMixin,CreateView):
	model = Project
	template_name = 'main/project_form.html'
	fields = [
		'project_name',
		'comment',
		'head',
		'members',
		
	]

	def form_valid(self,form):
		form.instance.head = self.request.user
		return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin,DeleteView):
	model = Project
	template_name = 'main/delete_project.html'
	
	
	success_url = '/trello/project/'


def show(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
	cont = {
		"form":form,
	}
	return render(request,"main/add.html",cont)

# def product_create_view(request):
# 	form = ProductForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()

# 	context = {
# 		'form':form,
# 	}
# 	return render(request,"form/product_create.html",context)

# def display(request):

def display(request):
	tasks = Task.objects.all()
	co = {
		'tasks':tasks,
	}

	return render(request,'main/show.html', co)


