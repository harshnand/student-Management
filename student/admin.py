from django.contrib import admin
from .models import Add_Student,Compant_details,Add_placement
from django.utils.html import format_html

# Register your models here.
# class AddstudentAdmin(admin.ModelAdmin):
#     # def thumbnail(self,object):
#     #     return format_html('<img src="{}" width="40" > .format(object.photo.url)')
#
#     list_display = ('id','thumbnail','name')


admin.site.register(Add_Student)
admin.site.register(Compant_details)
admin.site.register(Add_placement)