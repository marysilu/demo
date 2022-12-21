from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        firstnme = request.POST['fname']
        lastnme = request.POST['lname']
        emailid = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if firstnme == "":
            messages.info(request, "Enter first name")
            return redirect('register')
        elif lastnme == "":
            messages.info(request, "Enter last name")
            return redirect('register')
        elif emailid == "":
            messages.info(request, "Enter email id")
            return redirect('register')
        elif username == "":
            messages.info(request, "Enter username")
            return redirect('register')
        elif password == "":
            messages.info(request, "Enter password")
            return redirect('register')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                # print('user already exists')
                messages.info(request, "User already registered")
                return redirect('register')
            elif User.objects.filter(email=emailid).exists():
                # print('email id already registered')
                messages.info(request, "Email id already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=firstnme, last_name=lastnme, email=emailid,
                                                password=password, username=username)
                user.save()
                # print("User created")
                messages.info(request, "User created")
                return redirect('login')
        else:
            print("Password mismatch")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')
