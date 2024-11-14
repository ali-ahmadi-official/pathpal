from django import forms

class SmsSearchForm(forms.Form):
    product = forms.CharField(required=False, max_length=200)
    color = forms.CharField(required=False, max_length=100)
    date = forms.CharField(required=False, max_length=10)
