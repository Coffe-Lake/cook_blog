from functools import partial
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(max_length=100)
    parent = models.ForeignKey(
        'self', 
        related_name="children", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "категории"
        verbose_name_plural = "категории"

    def __str__(self):
        return f'{self.name[:40]}...'
    
    
class Tag(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    slug = models.SlugField(max_length=50)
    