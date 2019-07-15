from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import User
from .forms import CreateUser
from django.shortcuts import redirect
def index(request):
    return HttpResponse("Hello! You're at the cs411 project webpage.")

def base(request):
    return render(request, 'project/base.html')

def signup(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponse("Submitted!!")
    else:
        form = CreateUser()
    return render(request, 'project/signup.html', {'form': form})
