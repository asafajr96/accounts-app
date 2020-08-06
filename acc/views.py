from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from .forms import CreateUserForm

@csrf_exempt
def register(request):
	form = CreateUserForm()


	if request.method =='POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()

	context = {"form":form}
	return render(request, "register.html", context)

@csrf_exempt
def login(request):
	context = {}
	return render(request, "login.html", context)

