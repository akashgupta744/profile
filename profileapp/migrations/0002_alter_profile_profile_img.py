# Generated by Django 4.2.7 on 2024-01-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='media/default.jpg', null=True, upload_to='media'),
        ),
    ]
