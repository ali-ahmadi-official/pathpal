from django.db import models
from account.models import User

class Sms(models.Model):
    MONTH_CHOICES = (
        ("1", "فروردین"),
        ("2", "اردیبهشت"),
        ("3", "خرداد"),
        ("4", "تیر"),
        ("5", "مرداد"),
        ("6", "شهریور"),
        ("7", "مهر"),
        ("8", "آبان"),
        ("9", "آذر"),
        ("10", "دی"),
        ("11", "بهمن"),
        ("12", "اسفند"),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sms_author")
    product = models.CharField(max_length=200, default='')
    color = models.CharField(max_length=100, default='')
    characteristic = models.CharField(max_length=300, default='')
    day = models.IntegerField(default=1)
    month = models.CharField(max_length=2, choices=MONTH_CHOICES, default='1')
    year = models.IntegerField(default=1403)
    number = models.IntegerField(default=0)
    price = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.product
    
    def date_join(self):
        return f"{self.year}/{self.month}/{self.day}"

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
    field_4 = models.TextField(max_length=100, verbose_name='متن جای خالی چهارم', default='')

    def __str__(self):
        return 'محتوای سایت'