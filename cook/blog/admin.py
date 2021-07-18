from django.contrib import admin
from .models import Tag, Category
from mptt.models import MPTTModel


# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)