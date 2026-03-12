from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("Login Successful")
        else:
            return HttpResponse("Invalid crendentials")
    return render(request, "login.html")


# Create your views here.
