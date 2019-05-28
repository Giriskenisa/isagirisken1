# Generated by Django 2.2.1 on 2019-05-26 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_link', models.CharField(default='Eklenmemiş', max_length=100)),
                ('facebook_link', models.CharField(default='Eklenmemiş', max_length=100)),
                ('instagram_link', models.CharField(default='Eklenmemiş', max_length=100)),
                ('profil_foto', models.ImageField(blank=True, upload_to='media/profil')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
