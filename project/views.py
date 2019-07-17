from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import User
from .forms import CreateUser, InsertGEO
from django.shortcuts import redirect

from django.db import connection
def index(request):
    return HttpResponse("Hello! You're at the cs411 project webpage.")

def base(request):
    return render(request, 'project/base.html')

def signup(request):
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            username0 = form['username'].value();
            passward0 = form['password'].value();
            insert_query = 'INSERT INTO project_user (username,password) VALUES (%s, %s);'
            with connection.cursor() as cursor:
                cursor.execute(insert_query, (username0, passward0))
            return HttpResponse(username0)
    else:
        form = CreateUser()
    return render(request, 'project/signup.html', {'form': form})


def insert(request):
    if request.method == "POST":
        form = InsertGEO(request.POST)
        if form.is_valid():
            GEOID0 = form['GEOID'].value();
            Block0 = form['Block'].value();
            Population0 = form['Population'].value();
            insert_query = 'INSERT INTO tidychampaign1 (GEOID, Block, Population) VALUES (%s, %s, %s);'
            with connection.cursor() as cursor:
                cursor.execute(insert_query, (GEOID0, Block0, Population0))
            return HttpResponse("A new community submitted. The ID is " + GEOID0)
    else:
        form = InsertGEO()
    return render(request, 'project/insertGEO.html', {'form': form})
