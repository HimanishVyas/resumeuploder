from django.contrib import admin
from .models import resume
# Register your models here.

@admin.register(resume)

class resumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']
    