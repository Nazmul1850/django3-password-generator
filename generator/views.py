from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home1.html')

def password(request):
    thepassword = ''
    length = int(request.GET.get('length'))
    charecter = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        charecter.extend(list('ABCDEFHIJKLMNOPQRSTUVWXUZ'))
    if request.GET.get('number'):
        charecter.extend(list('1234567890'))
    if request.GET.get('special'):
        charecter.extend(list('!@#$%^&*|?><'))
    for x in range(length):
        thepassword += random.choice(charecter)
    return render(request, 'generator/password.html',{'password' : thepassword})

def about(request):
    return render(request,'generator/about.html')
