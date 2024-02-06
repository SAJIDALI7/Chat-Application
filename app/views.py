from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm
from django.contrib.auth.views import LoginView
# from .models import Profile
# Create your views here.


def home(request):
    return render(request, 'app/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('login')
        
    else:
        form = SignupForm()
    return render(request, 'app/singup.html', {'form': form})

class LOginuser(LoginView):
    template_name = 'app/login.html'
    success_url = 'home'


def logouserout(request):
    logout(request)
    return redirect('home')

# def profilephotoform(request):
#     if request.method == "POST":
#         form = PhotoForm(request.POST, request.FILES, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = PhotoForm()
#     return render(request, 'app/photo.html', {'form': form})
