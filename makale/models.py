from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MaxLengthValidator,MinLengthValidator
# Create your models here.

class Makale(models.Model):
    yazar = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    baslik = models.CharField(max_length=100)
    icerik = models.TextField(validators=[MinLengthValidator(100), MaxLengthValidator(500)])
    yazilma_tarihi = models.DateTimeField(default=timezone.now)
    makale_foto = models.FileField(verbose_name="Fotoğraf Ekle")
    like = models.IntegerField(default=0)
    viewed = models.IntegerField(default=0)
    def __str__(self):
        return self.baslik

    class Meta:
        ordering = ['-yazilma_tarihi']

class Yorum(models.Model):
    makale = models.ForeignKey(Makale,on_delete=models.CASCADE,verbose_name="Makale",related_name="yorumlar")
    yorum_sahibi = models.ForeignKey(settings.AUTH_USER_MODEL,max_length=50,verbose_name="isim",on_delete=models.CASCADE)
    yorum_text = models.CharField(max_length=250,verbose_name="yorum")
    yorum_tarih = models.DateTimeField(default=timezone.now)
    models.IntegerField()
    def __str__(self):
        return self.yorum_text

    class Meta:
        ordering = ['-yorum_tarih']

class favori(models.Model):
    makale = models.ForeignKey(Makale,on_delete=models.CASCADE)
    liked_post_id = models.IntegerField()
    liked_by = models.IntegerField()
    liked_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.makale.baslik