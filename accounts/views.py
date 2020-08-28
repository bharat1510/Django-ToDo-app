from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . import models
from django.conf import settings

from .forms import TodoForm 
from .models import Todo

# Create your views here.
def index(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == 'GET':
		return render(request,'signup.html')
	else:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['pass']
		password1 = request.POST['pass1']
		if password==password1:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username is taken")
				return redirect('signup')
			elif User.objects.filter(email=email).exists():
				messages.error(request,"Email id is already registered")
				return redirect('signup')
			else:
				user = User.objects.create_user(password=password,username=username,email=email)
				user.save()
				return redirect('login')
		else:
			messages.warning(request,"Password not match")
			return redirect('signup')
		return redirect('/')
				
	#return render(request, 'signup.html')

def login(request):
	if request.method == 'GET':
		return render(request,'login.html')
	else:
		username = request.POST['username']
		password = request.POST['pass']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.warning(request,"Check your Username or Password.")
			return redirect('login')
			
	#return render(request, 'login.html')
	
def logout(request):
	auth.logout(request)
	return redirect('/')
	
def base(request):
	item_list = Todo.objects.order_by("-date") 
	if request.method == "POST": 
		form = TodoForm(request.POST) 
		if form.is_valid(): 
			form.save() 
			messages.success(request, "Item added !!!") 
			return redirect('base') 
	form = TodoForm() 

	page = { 
			"forms" : form, 
			"list" : item_list, 
			"title" : "TODO App", 
		} 
	return render(request, 'base.html', page)

def remove(request, item_id): 
	item = Todo.objects.get(id=item_id) 
	item.delete() 
	messages.info(request, "Item removed !!!") 
	return redirect('/') 