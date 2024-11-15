from django import forms

class SmsSearchForm(forms.Form):
    product = forms.CharField(required=False, max_length=200)
    color = forms.CharField(required=False, max_length=100)
    day = forms.IntegerField(required=False)
    month = forms.CharField(required=False, max_length=2)
    year = forms.IntegerField(required=False)
