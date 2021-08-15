from django import template
from blog.models import Category, Post

register = template.Library()


# @register.simple_tag()
# def get_categories():
    ## Вывод всех категорий
#     return Category.objects.all()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories(count=5):
    category = Category.objects.order_by("name")[:count]
    return {"list_category": category}