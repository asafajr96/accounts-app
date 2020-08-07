from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .forms import CreateUserForm

@csrf_exempt
def registerpage(request):
	form = CreateUserForm()


	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get("username") #pulls saved username from the form.
			messages.success(request, "Account was created for " + user) #Saved user confirmation message.
			return redirect("login")

	context = {"form":form}
	return render(request, "register.html", context)

@csrf_exempt
def loginpage(request):

	if request.method =="POST":
		username = request.POST.get("username_txt")
		password = request.POST.get("password_txt")

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect("register")
		else:
			messages.info(request, "Incorrect login details! Please try again.")
			


	context = {}
	return render(request, "login.html", context)

