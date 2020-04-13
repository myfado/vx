from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home_page(request):
    welcome = 'Welcome!'
    if request.user.is_authenticated:
        user = (User.objects.get(username=request.user.username))
        welcome="Welcome"
    context = {"welcome": welcome, "username":str(user).capitalize()}
    return render(request, "home.html", context)
