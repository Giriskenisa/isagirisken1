# Generated by Django 2.2.1 on 2019-05-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profil_foto',
            field=models.ImageField(blank=True, upload_to='profil'),
        ),
    ]
