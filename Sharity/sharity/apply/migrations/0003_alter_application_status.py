# Generated by Django 3.2.13 on 2022-04-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_alter_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Inprocess', 'Inprocess'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Inprocess', max_length=100),
        ),
    ]