from django.shortcuts import render, reverse
from django.http import JsonResponse,HttpResponseRedirect
from .models import *
from django.db.models import Sum
import json

# Create your views here.

def NewQuestionPage(request):
    return render(request,'stack_enterprise/new-post.html')

def LoginPage(request):
    if 'user_id' in request.session:
        return render(request,'stack_enterprise/base.html')
    else:
        return render(request,'stack_enterprise/login.html')
def UserLogout(request):
    try:
        del request.session['user_id']
        del request.session['username']
        return HttpResponseRedirect(reverse('user-logout'))
    except:
        return HttpResponseRedirect(reverse('login'))

def HomePage(request):
    all_questions = Questions.objects.all().prefetch_related('owner_id','answers_set','upvotes_set').order_by('-created_at')[:25]
    top_questions = []
    for question in all_questions:
        answers = question.answers_set.filter().count()
        upvotes = question.upvotes_set.filter().aggregate(Sum('vote_count'))
        question_data = dict()
        question_data['id'] = question.id
        question_data['title'] = question.title
        question_data['tags'] = question.tags
        question_data['user'] = question.owner_id.username
        question_data['upvotes'] = upvotes
        question_data['answers'] = answers
        question_data['created_at'] = question.created_at
        top_questions.append(question_data)
    print(top_questions)
    return render(request,'stack_enterprise/base.html',{'top_questions':top_questions})


def UserLogin(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username = request.POST['username'])
            print(user)
            if user.username == request.POST['username'] and user.password == request.POST['password']:
                print('inside if')
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return HttpResponseRedirect(reverse('home-page'))
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

def QuestionPage(request):
    questions = Questions.objects.filter(pk = request.GET['question_id']).select_related('owner_id')
    all_answers = Answers.objects.filter( question_id = request.GET['question_id']).select_related('user_id')
    for question in questions:
        question_data = dict()
        question_data['id'] = question.id
        question_data['title'] = question.title
        question_data['user_id'] = question.owner_id.username
        question_data['reputation'] = question.owner_id.reputation
        question_data['body'] = question.body
        question_data['ans_count'] = Answers.objects.filter(question_id = request.GET['question_id']).count()
        answers = []
        for answer in all_answers:
            upvotes = Upvotes.objects.filter(answer_id = answer.id).aggregate(Sum('vote_count'))
            ans = dict()
            ans['id'] = answer.id
            ans['details']= answer.details
            ans['user_id'] = answer.user_id.username
            ans['created_at'] = answer.created_at
            ans['upvotes'] = upvotes
            comments = []
            all_comments = Comments.objects.filter(answer_id = answer.id).select_related('user_id')
            for comment in all_comments:
                comm = dict()
                comm['id'] = comment.id
                comm['comment'] = comment.comment
                comm['user_id'] = comment.user_id.username
                comm['created_at'] = comment.created_at
                comments.append(comm)
            ans['comments'] = all_comments
            answers.append(ans)
        question_data['answers'] = answers
    print(question_data)
    return render(request,'stack_enterprise/question.html',{'question_data':question_data})