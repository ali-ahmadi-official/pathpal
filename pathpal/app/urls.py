from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import view, signup, phone_login_view, SmsCreateView, SmsDeleteView

app_name = 'app'

urlpatterns = [
    path('', view, name='sms_list'),
    path('signup/', signup, name='signup'),
    path('login/', phone_login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', SmsCreateView.as_view(), name='sms_create'),
    path('delete/<int:pk>/', SmsDeleteView.as_view(), name='sms_delete'),
]