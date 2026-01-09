from django.shortcuts import render

from django.shortcuts import redirect


def root(request):
    return redirect("/login/")

def signup(request):
    return render(request, "signup.html")

def login_view(request):
    return render(request, "login.html")

def home(request):
    return render(request, "home.html")

def add_task(request):
    return render(request, "add-task.html")

def task_detail(request, id):
    return render(request, "task-detail.html")

def edit_task(request, id):
    return render(request, "edit-task.html")

def profile(request):
    return render(request, "profile.html")

def reset_password(request):
    return render(request, "reset-password.html")
