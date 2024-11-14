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

def view(request):
    smss = Sms.objects.all()
    users = User.objects.all()
    form = SmsSearchForm(request.GET)
    content = Content.objects.get(id=1)

    if form.is_valid():
        product = form.cleaned_data.get('product')
        color = form.cleaned_data.get('color')
        date = form.cleaned_data.get('date')
        
        if product:
            smss = smss.filter(product__icontains=product)
        if color:
            smss = smss.filter(color__icontains=color)
        if date:
            smss = smss.filter(date__icontains=date)

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
            form.save()
            return redirect('app:sms_list')
        else:
            return render(request, 'app/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

class SmsCreateView(LoginRequiredMixin, CreateView):
    model = Sms
    fields = ['product', 'color', 'characteristic', 'date', 'number', 'price']
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
