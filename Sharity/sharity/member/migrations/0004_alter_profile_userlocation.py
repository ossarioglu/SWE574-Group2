# Generated by Django 3.2.13 on 2022-04-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_merge_0002_alter_profile_userpicture_0002_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='userLocation',
            field=models.TextField(),
        ),
    ]
