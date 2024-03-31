from django.contrib import admin
from .models import studentDetails
# Register your models here.
class ApplyDetail(admin.ModelAdmin):
    list_display = ('name', 'University', 'branch', 'session', 'email', 'phone', 'Password')  # Adjust the attributes accordingly

admin.site.register(studentDetails,ApplyDetail)


