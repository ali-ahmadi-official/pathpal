# Generated by Django 5.1.3 on 2024-11-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='default_user', max_length=150, unique=True, verbose_name='phone number'),
        ),
    ]
