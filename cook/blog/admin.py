from django.contrib import admin
from django.db.models.base import Model
from mptt.admin import MPTTModelAdmin


from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', "prep_time", "cook_time", "post"]
    save_as = True
    save_on_top = True


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', "email", "post"]


@admin.register(models.Category)
class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


