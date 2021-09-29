from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        password1 = request.POST['password1']
        email = request.POST['email']

        if password == password1:
            if User.objects.filter(username=username).exists():
                print('username taken')
            elif User.objects.filter(email=email).exists():
                print('email taken')
            else:
                user = User.objects.create_user(username=username ,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();

        else:
            print('not matching')
        return redirect('/')

    else:
        return render(request,'signup.html')
