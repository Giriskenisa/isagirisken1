from django.shortcuts import render,redirect,get_object_or_404,reverse
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Makale,Yorum,favori
from django.db.models import Q
from user.models import User,UserProfile,create_profile


# Create your views here.
def paylasimlar(request):
    keyword = request.GET.get("keyword")
    if keyword:
        paylasimlar = Makale.objects.filter(Q(baslik__contains=keyword) | Q(icerik__contains=keyword))
        return render(request, "feed.html", {"paylasimlar": paylasimlar})
    paylasimlar = Makale.objects.all()
    if request.user.is_authenticated and request.user is not None:
        userprofile = UserProfile.objects.filter(user=request.user).first()
        if userprofile is None:
            request.session["profil"] = False
        else:
            request.session["profil"] = True
    return render(request, "feed.html", {"paylasimlar":paylasimlar})


def index(request):
    return redirect("paylasimlar")

@login_required(login_url="user:login")
def dashboard(request):
    makaleler = Makale.objects.filter(yazar=request.user)
    profil = UserProfile.objects.filter(user = request.user).first()
    return render(request, "dashboard.html",{"makaleler":makaleler,"user":profil})

@login_required(login_url="user:login")
def makale_ekle(request):
    form = forms.MakaleForm(request.POST,request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            makale = form.save(commit=False)
            makale.yazar = request.user
            makale.save()
            messages.success(request,"Makale Yayınlandı")
            return redirect("dashboard")
        else:
            messages.info(request,"Giriş Alanı Hatalı Lütfen Tekrar Deneyiniz")
            return render(request,"makale_ekle.html",{"form":form})

    else:
        context = {
            "form": form,
        }
        return render(request,"makale_ekle.html",context)

@login_required(login_url="user:login")
def detay(request,id):
    #makale = Makale.objects.filter(id=id).first()
    makale = get_object_or_404(Makale,id=id)
    makale.viewed +=1
    makale.save()
    makale_sayisi = Makale.objects.filter(yazar=makale.yazar).count()
    yorumlar = Yorum.objects.filter(makale = makale)
    fav = favori.objects.filter(liked_by = request.user.id,liked_post_id = id).first()
    return render(request,"detay.html",{"makale":makale,"makale_sayisi":makale_sayisi,"yorumlar":yorumlar,"fav":fav})

def like_makale(request,id):
    fav = favori.objects.filter(liked_by =request.user.id,liked_post_id =id).first()
    if fav is None:
        makale = get_object_or_404(Makale, id=id)
        makale.like += 1
        makale.save()
        newFav = favori()
        newFav.makale = makale
        newFav.liked_by = request.user.id
        newFav.liked_post_id = makale.id
        newFav.save()
    return redirect(reverse("detay",kwargs={"id":id}))

@login_required(login_url="user:login")
def guncelle(request,id):
    makale = get_object_or_404(Makale,id=id)
    form = forms.MakaleForm(request.POST or None,request.FILES or None,instance=makale)
    if request.method == "POST" and form.is_valid():
        makale = form.save(commit=False)
        makale.yazar = request.user
        makale.save()
        messages.success(request,"Makale Başarı İle Güncellendi")
        return redirect("dashboard")
    else:
        return render(request,"guncelle.html",{"form":form,"makale":makale})

@login_required(login_url="user:login")
def sil(request,id):
    makale = get_object_or_404(Makale,id=id)
    makale.delete()
    messages.success(request,"Paylaşım Silindi")
    return redirect("dashboard")

@login_required(login_url="user:login")
def yorum_ekle(request,id):
    makale = get_object_or_404(Makale,id=id)
    if request.method == "POST":
        yorum_icerik = request.POST.get("yorum_icerik")

        yorum = Yorum(yorum_text=yorum_icerik)
        yorum.yorum_sahibi = request.user
        yorum.makale = makale
        yorum.save()
        messages.success(request, "Yorumunuz eklenmiştir..")
        return redirect(reverse("detay",kwargs={"id":id}))

@login_required(login_url="user:login")
def yorum_sil(request,yorum_id,makale_id):
    yorum = Yorum.objects.filter(id=yorum_id)
    yorum.delete()
    messages.success(request,"Yorumunuz silinmiştir.")
    return redirect("detay",id=makale_id)

def favoriler(request):
    favoriler = favori.objects.filter(liked_by=request.user.id)
    return render(request,"favoriler.html",{"favoriler":favoriler})

def favori_sil(request,id):
    fav = favori.objects.filter(id=id).first()
    makale = Makale.objects.filter(id = fav.liked_post_id).first()
    makale.like -= 1
    makale.save()
    fav.delete()
    return redirect("favoriler")

def yazar_profil(request,username):
    user = User.objects.filter(username=username).first()
    makaleler = Makale.objects.filter(yazar=user)
    profil = UserProfile.objects.filter(user=user).first()
    return render(request, "yazar_profil.html", {"makaleler": makaleler, "user": profil})





