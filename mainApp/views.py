from contextlib import redirect_stderr
import bcrypt
from django.contrib import messages
from django.shortcuts import redirect, render, HttpResponse
from .models import *

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        errors = Users.objects.validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['password']
            pwHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            newUser = Users.objects.create(username=username,fname=fname,lname=lname,email=email,password=pwHash)
            newUser.save()
            request.session['loggedInUser'] = newUser.id
            return redirect(f'/{username}')

def login(request):
    if request.method=='POST':
        users = Users.objects.filter(email__iexact=request.POST['email'])
        if len(users)==1:
            if not bcrypt.checkpw(request.POST['password'].encode(),users[0].password.encode()):
                messages.error(request, "Email or Password is incorrect!")
                return redirect('/')
            else:
                request.session['loggedInUser'] = users[0].id
                user = Users.objects.get(id=request.session['loggedInUser'])
                return redirect(f'/{user.username}')
        else:
            messages.error(request, "Email does not exist!")
            return redirect('/')
            

def profile(request,username):
    context={
        'loggedInUser':Users.objects.get(id=request.session['loggedInUser']),
        'user':Users.objects.get(username=username),
        'posts':Users.objects.get(username=username).posts.order_by('-createdAt')
    }
    return render(request,'profilePage.html',context)

def logout(request):
    request.session.clear()
    return redirect('/')

def createPost(request):
    if request.method == 'POST':
        user = Users.objects.get(id=request.session['loggedInUser'])
        errors = Posts.objects.validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/{user.username}')
        else:
            content = request.POST['content']
            newPost = Posts.objects.create(content=content,user=user)
            newPost.save()
            return redirect(f'/{user.username}')

def deletePost(request,id):
    user = Users.objects.get(id=request.session['loggedInUser'])
    post = Posts.objects.get(id=id)
    post.delete()
    return redirect(f'/{user.username}')

def feed(request):
    context={
        'loggedInUser':Users.objects.get(id=request.session['loggedInUser']),
        'posts':Posts.objects.all().order_by('-createdAt')
    }
    return render(request,'feed.html',context)
