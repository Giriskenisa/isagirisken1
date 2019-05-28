from django.contrib import admin
from .models import Makale,Yorum,favori
# Register your models here.

@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ["baslik","yazilma_tarihi"]
    search_fields = ["baslik","yazar"]
    list_display_links = ["baslik","yazilma_tarihi"]
    class Meta:
        model = Makale

admin.site.register(Yorum)
admin.site.register(favori)

