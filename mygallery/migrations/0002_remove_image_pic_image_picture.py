# Generated by Django 4.0.3 on 2022-03-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mygallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pic',
        ),
        migrations.AddField(
            model_name='image',
            name='picture',
            field=models.ImageField(null=True, upload_to='Image/'),
        ),
    ]
