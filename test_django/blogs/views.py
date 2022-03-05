from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages


def hello(request):
    # Query data from model
    data = Post.objects.all()
    return render(request, 'index.html', {'data': data})


def register(request):
    g = "Welcome to Page1"

    return render(request, 'page1.html',
                  {
                      'g': g
                  })


def createform(request):
    return render(request, 'form.html')


def addblogs(request):
    name = request.POST['name']
    article = request.POST['description']
    return render(request, 'result.html',
                  {
                      'name': name,
                      'article': article
                  })


def adduserdata(request):
    username = request.POST['username']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:

        if User.objects.filter(username=username):
            messages.info(request, '*Username นี้มีคนใช้แล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, '*Email นี้เคยลงทะเบียนแล้ว')
            return redirect('/register')
        else:

            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.save()

        return redirect('/')
    else:
        messages.info(request, '*Password ไม่ตรงกัน')
        return redirect('/register')


def loginuser(request):

    return render(request, 'login.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password1']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'ไม่พบข้อมูล')
        return redirect('/loginform')

def logout(request):
    auth.logout(request)
    return redirect('/')
