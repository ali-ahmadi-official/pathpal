from django.db import models
from account.models import User

class Sms(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sms_author")
    product = models.CharField(max_length=200, default='')
    color = models.CharField(max_length=100, default='')
    characteristic = models.CharField(max_length=300, default='')
    date = models.CharField(max_length=10, default='')
    number = models.IntegerField(default=0)
    price = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.product

class Content(models.Model):
    logo = models.TextField(max_length=200, verbose_name='متن لوگو ها')
    header_p = models.TextField(max_length=800, verbose_name='متن بالای صفحه')
    search_u_p = models.TextField(max_length=800, verbose_name='متن بالای باکس سرچ')
    search_d_p = models.TextField(max_length=800, verbose_name='متن پایین باکس سرچ')
    add_u_p = models.TextField(max_length=800, verbose_name='متن بالای باکس ادد')
    add_d_p = models.TextField(max_length=800, verbose_name='متن پایین باکس ادد')
    field_1 = models.TextField(max_length=100, verbose_name='متن جای خالی اول')
    field_2 = models.TextField(max_length=100, verbose_name='متن جای خالی دوم')
    field_3 = models.TextField(max_length=100, verbose_name='متن جای خالی سوم')

    def __str__(self):
        return 'محتوای سایت'