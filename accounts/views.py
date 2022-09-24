from django.shortcuts import render,redirect
from . models import *
from . models import User

# Create your views here.

def signup(request):
   return render(request,'register.html')
               
               
def loginpage(request):
   return render(request,'login.html')


def logout(request):
   return render(request,'login.html')