from django.shortcuts import render, reverse
from django.http import JsonResponse,HttpResponseRedirect
from .models import *
import json

# Create your views here.

def HomePage(request):
    all_questions = Questions.objects.all().select_related().order_by('-created_at')
    return render(request,'stack_enterprise/base.html',{'all_questions':all_questions})

def NewQuestionPage(request):
    return render(request,'stack_enterprise/new-post.html')

def LoginPage(request):
    if 'user_id' in request.session:
        return render(request,'stack_enterprise/base.html')
    else:
        return render(request,'stack_enterprise/login.html')

def UserLogin(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            print(user)
            if user.username == request.POST['username'] and user.password == request.POST['password']:
                print('inside if')
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return render(request,'stack_enterprise/base.html')
            else:
                print('inside else')
                return render(request,'stack_enterprise/login.html',{'error':'username or password invalid.'})

        except Exception:
            return render(request,'stack_enterprise/login.html',{'error':'user doesnt exist.Please register!'})

def CreateNewQuestion(request):
    if request.method == 'POST':
        if 'user_id' in request.session:
            title = request.POST['title']
            tags = request.POST['tags']
            body = request.POST['description']
            try:
                owner_id = User.objects.get(pk = request.session['user_id'])
                question = Questions.objects.create(title=title,body=body,tags=tags,owner_id=owner_id)
                owner_id.reputation = owner_id.reputation + 1
                owner_id.save()
                return render(request,'stack_enterprise/base.html',{'question':question})
            except:
                return render(request,'stack_enterprise/login.html',{'error':'user doesnt exist.Please register!'})
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(reverse('new_question'))

def UserLogout(request):
    try:
        del request.session['user_id']
        del request.session['username']
        return HttpResponseRedirect(reverse('user-logout'))
    except:
        return HttpResponseRedirect(reverse('login'))