from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('makale_ekle/',views.makale_ekle,name="makale_ekle"),
    path('detay/<int:id>',views.detay,name="detay"),
    path('guncelle/<int:id>',views.guncelle,name="guncelle"),
    path('sil/<int:id>',views.sil,name="sil"),
    path('feed',views.paylasimlar,name="paylasimlar"),
    path('yorum_ekle/<int:id>',views.yorum_ekle,name="yorum_ekle"),
    path('yorum_sil/<int:yorum_id>/<int:makale_id>',views.yorum_sil,name="yorum_sil"),
    path('like_makale/<int:id>',views.like_makale,name="like_makale"),
    path('favoriler/',views.favoriler,name="favoriler"),
    path('favori_sil/<int:id>',views.favori_sil,name="favori_sil"),
    path('yazar_profil/<slug:username>',views.yazar_profil,name="yazar_profil"),
]
