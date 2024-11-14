from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib import messages

from account.forms import CustomeUserCreationForm, PhoneLoginForm
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
        signup = CustomeUserCreationForm(request.POST)
        if signup.is_valid():
            signup.save()
            return redirect('app:sms_list')
    else:
        signup = CustomeUserCreationForm()
    
    return render(request, 'app/signup.html', {'signup': signup})


def phone_login_view(request):
    if request.method == "POST":
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            try:
                user = form.authenticate()
                if user:
                    login(request, user)
                    messages.success(request, "Logged in successfully!")
                    return redirect('app:sms_list')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PhoneLoginForm()

    return render(request, "app/login.html", {"form": form})

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
