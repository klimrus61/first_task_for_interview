from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse


def login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        return redirect(reverse('login_page'))
    return render(request, "login.html")
