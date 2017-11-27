from django.contrib import admin
from . import models
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    search_fields = ['username','email_address']
    model = models.User

class LoginInstanceAdmin(admin.ModelAdmin):
    search_fields = ['username','date']
    model = models.LoginInstance

class LogoutInstanceAdmin(admin.ModelAdmin):
    search_fields = ['username','date']
    model = models.LogoutInstance

admin.site.register(models.User, UserAdmin)
admin.site.register(models.LoginInstance, LoginInstanceAdmin)
admin.site.register(models.LogoutInstance, LogoutInstanceAdmin)
