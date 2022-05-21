# Generated by Django 3.2.13 on 2022-05-10 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermessages', '0003_usermessage_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermessage',
            name='parent',
        ),
        migrations.AddField(
            model_name='usermessage',
            name='child',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='usermessages.usermessage'),
        ),
    ]
