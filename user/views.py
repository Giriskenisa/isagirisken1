from django.shortcuts import render,redirect
from . import forms
import django.contrib.sessions
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import UserProfile

def register(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST,request.FILES or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            new_user = User(username=username,email=email)
            new_user.set_password(password)
            try:
                new_user.save()
                login(request, new_user)
                messages.success(request, "Başarı ile Kayıt Olundu")
                return redirect("makale:feed")
            except:
                messages.info(request,"Kullanıcı adı veya mail alınmış")
                return redirect("user:register")


        else:
            context = {
                "form":form
            }
            return render(request, "register.html", context)
    else:
        form = forms.RegisterForm()
        context = {
            "form":form
        }
        return render(request,"register.html",context)

def login(request):
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username,password=password)

            if user is None:
                messages.info(request,"Kullanıcı Adı Veya Parola Hatası")
                return render(request,"login.html",context)
            messages.success(request,"Hoşgeldiniz "+ username)
            dj_login(request,user)
            return redirect("/makale/feed")
        return render(request, "login.html", context)

    else:
        form = forms.LoginForm()
        if request.user.is_authenticated:
            return redirect("makale")
        context ={
            "form":form
        }
        return  render(request,"login.html",context)

def logout(request):
    django_logout(request)
    messages.success(request,"Çıkış Yapıldı")
    return redirect("index")

@login_required(login_url="user:login")
def profil_duzenle(request):
    bilgiler = UserProfile.objects.filter(user=request.user).first()
    form = forms.UserProfileForm(request.POST or None,request.FILES or None,instance=bilgiler)
    context = {
        "form":form,
        "bilgiler":bilgiler,
    }
    if request.method == "POST":
        is_there = UserProfile.objects.get(user=request.user)
        profil = form.save(commit=False)
        is_there.twitter_link = profil.twitter_link
        is_there.facebook_link = profil.facebook_link
        is_there.instagram_link = profil.instagram_link
        is_there.profil_foto = profil.profil_foto
        is_there.save()
        return redirect("dashboard")

    else:
        return render(request,"profil_duzenle.html",context)

