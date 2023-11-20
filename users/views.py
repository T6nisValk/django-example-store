from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import User

# Create your views here.


def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists!")
            return redirect("register")

        User.objects.create_user(username=username, email=email, first_name=name, last_name=surname, password=password)
        return redirect("home")
    return render(request, "registration/register.html")
