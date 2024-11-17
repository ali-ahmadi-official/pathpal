from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy

from account.forms import CustomUserCreationForm
from account.models import User

from .models import Sms, Content
from .forms import SmsSearchForm
from .jalaly import Persian

def view(request):
    today = datetime.today().date()
    smss = Sms.objects.all()
    for sms in smss:
        output = Persian(sms.year, sms.month, sms.day).gregorian_datetime()
        if output < today:
            sms.delete()

    users = User.objects.all()
    form = SmsSearchForm(request.GET)
    content = Content.objects.get(id=1)

    if form.is_valid():
        product = form.cleaned_data.get('product')
        color = form.cleaned_data.get('color')
        day = form.cleaned_data.get('day')
        month = form.cleaned_data.get('month')
        year = form.cleaned_data.get('year')
        
        if product:
            smss = smss.filter(product__icontains=product)
        if color:
            smss = smss.filter(color__icontains=color)
        if day:
            smss = smss.filter(day=day)
        if month:
            smss = smss.filter(month=month)
        if year:
            smss = smss.filter(year=year)

    context = {
        'smss': smss,
        'users': users,
        'form': form,
        'content': content,
    }

    return render(request, 'app/sms_list.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app:sms_list')
        else:
            return render(request, 'app/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

class SmsCreateView(LoginRequiredMixin, CreateView):
    model = Sms
    fields = ['product', 'color', 'characteristic', 'day', 'month', 'year', 'number', 'price']
    success_url = reverse_lazy('app:sms_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SmsDeleteView(LoginRequiredMixin, DeleteView):
    model = Sms
    success_url = reverse_lazy('app:sms_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        if self.request.user.is_superuser:
            return obj
        
        if obj.author != self.request.user:
            raise Http404("شما مجاز به حذف این پست نیستید.")
        
        return obj