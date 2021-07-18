from functools import partial
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']


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
        if len(self.name) > 30:
            return f"{self.name[:30]}..."
        else:
            return self.name
    
    
class Tag(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    slug = models.SlugField(max_length=50)
    
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"
        
    def __str__(self):
        if len(self.name) > 15:
            return f"{self.name[:15]}..."
        else:
            return self.name