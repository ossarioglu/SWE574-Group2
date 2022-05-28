# Generated by Django 3.2.13 on 2022-05-23 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_alter_profile_userpicture'),
        ('badges', '0002_auto_20220522_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greatserviceproviderbadge',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='GSPbadge', to='member.owner'),
        ),
        migrations.AlterField(
            model_name='mastereventorganizerbadge',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='MEObadge', to='member.owner'),
        ),
        migrations.AlterField(
            model_name='newcomerbadge',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Nbadge', to='member.owner'),
        ),
    ]