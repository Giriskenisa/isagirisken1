from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    twitter_link = models.CharField(blank=True,max_length=100,verbose_name="Twitter Kullanıcı Adı")
    facebook_link = models.CharField(blank=True,max_length=100,verbose_name="Facebook Kullanıcı Adı")
    instagram_link = models.CharField(blank=True,max_length=100, verbose_name="Instagram Kullanıcı Adı")
    profil_foto = models.ImageField(upload_to='profil',blank=True)
    def __str__(self):
        return self.user.username


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)