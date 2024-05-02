from django.shortcuts import render
import random
#from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def password(request):
    
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    password_generada = ''
    
    lenght = int(request.GET.get('lenght'))
    
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        caracteres.extend(list('-_+!@#$%&*()'))
        
    if request.GET.get('numbers'):
        caracteres.extend(list('0123456789'))
        
    
    for x in range(lenght):
        password_generada += random.choice(caracteres)
        
    return render(request, 'password.html',{'password' : password_generada})