# Generated by Django 5.1.3 on 2024-11-12 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='add_d_p',
            field=models.TextField(max_length=800, verbose_name='متن پایین باکس ادد'),
        ),
        migrations.AlterField(
            model_name='content',
            name='add_u_p',
            field=models.TextField(max_length=800, verbose_name='متن بالای باکس ادد'),
        ),
        migrations.AlterField(
            model_name='content',
            name='field_1',
            field=models.TextField(max_length=100, verbose_name='متن جای خالی اول'),
        ),
        migrations.AlterField(
            model_name='content',
            name='field_2',
            field=models.TextField(max_length=100, verbose_name='متن جای خالی دوم'),
        ),
        migrations.AlterField(
            model_name='content',
            name='field_3',
            field=models.TextField(max_length=100, verbose_name='متن جای خالی سوم'),
        ),
        migrations.AlterField(
            model_name='content',
            name='header_p',
            field=models.TextField(max_length=800, verbose_name='متن بالای صفحه'),
        ),
        migrations.AlterField(
            model_name='content',
            name='logo',
            field=models.TextField(max_length=200, verbose_name='متن لوگو ها'),
        ),
        migrations.AlterField(
            model_name='content',
            name='search_d_p',
            field=models.TextField(max_length=800, verbose_name='متن پایین باکس سرچ'),
        ),
        migrations.AlterField(
            model_name='content',
            name='search_u_p',
            field=models.TextField(max_length=800, verbose_name='متن بالای باکس سرچ'),
        ),
    ]
