# Generated by Django 3.2.13 on 2022-05-12 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_profile_userlocation'),
        ('usermessages', '0009_usermessage_inbox_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='inbox_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_inbox', to='member.profile'),
        ),
    ]