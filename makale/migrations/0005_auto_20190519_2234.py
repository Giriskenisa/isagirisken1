# Generated by Django 2.2.1 on 2019-05-19 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makale', '0004_auto_20190519_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='makale',
            options={'ordering': ['-yazilma_tarihi']},
        ),
        migrations.AlterModelOptions(
            name='yorum',
            options={'ordering': ['-yorum_tarih']},
        ),
    ]
