# Generated by Django 3.2.13 on 2022-05-21 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_profile_userlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userPicture',
            field=models.ImageField(default='male.png', null=True, upload_to='static/images/Profiles'),
        ),
    ]
