from django.contrib import admin

# Register your models here.
from webapp.models import Image, Comment

admin.site.register(Image)
admin.site.register(Comment)