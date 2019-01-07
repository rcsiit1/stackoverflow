from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from .models import *
import json

# Create your views here.

def HomePage(request):
    return render(request,'stack_enterprise/base.html')

def NewQuestionPage(request):
    return render(request,'stack_enterprise/new-post.html')

def LoginPage(request):
    return render(request,'stack_enterprise/login.html')

def UserLogin(request):
    if request.method == 'POST':
        try:
            if request.session['user_id'] == user.id:
                return HttpResponseRedirect(reverse())

            user = User.objects.get(username = request.POST['username'])

            if user.username == request.POST['username'] and user.password == request.POST['password']:
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return render(request,'stack_enterprise/base.html')
            else:
                return render(request,'stack_enterprise/login.html',{'error':'username or password invalid.'})

        except Exception:
            return render(request,'stack_enterprise/login.html',{'error':'user doesnt exist.Please register!'})