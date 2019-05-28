from django import forms
from .models import UserProfile
from django.forms import ModelForm
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,min_length=5,label="Kullanıcı Adı")
    email = forms.EmailField(label="E-Posta")
    password = forms.CharField(max_length=12,min_length=8,label="Parola",widget=forms.PasswordInput)
    confirm = forms.CharField(label="Parola Tekrar",widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password =self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password!=confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values ={
            "username":username,
            "email":email,
            "password":password,
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı Adı")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        values = {
            "username":username,
            "password":password
        }

        return values

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['twitter_link','instagram_link','facebook_link','profil_foto']