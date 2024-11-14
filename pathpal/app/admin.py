from django.contrib import admin
from .models import Sms, Content

class SmsAdmin(admin.ModelAdmin):
    list_display = ['product', 'color', 'characteristic', 'date', 'number', 'price', 'author']

class ContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return True

admin.site.register(Sms, SmsAdmin)
admin.site.register(Content)