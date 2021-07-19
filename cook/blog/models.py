from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(verbose_name="Название", max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        verbose_name="Родитель", 
        related_name="children", 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']
        
    class Meta:
        verbose_name = "категория"
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
        

class Post(models.Model):
    author = models.ForeignKey(
        User, 
        verbose_name="Автор",
        related_name="posts", 
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(verbose_name="Название", max_length=200)
    image = models.ImageField(verbose_name="Изображение", upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        verbose_name="Категория", 
        related_name="post", 
        on_delete=models.SET_NULL, 
        null=True,
    )
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name="post")
    create_at = models.DateTimeField(verbose_name="Дата", auto_now_add=True)

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        
    def __str__(self):
        if len(self.title) > 15:
            return f"{self.title[:15]}..."
        else:
            return self.title
        
    
class Recipe(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100)
    service = models.CharField(verbose_name="Затрачиваемое время", max_length=50)
    prep_time = models.PositiveIntegerField(verbose_name="Время подготовки", default=0)
    cook_time = models.PositiveIntegerField(verbose_name="Время приготовления", default=0)
    ingredients = models.TextField(verbose_name="Ингредиенты")
    directions = models.TextField(verbose_name="Руководство по приготовлению")
    post = models.ForeignKey(
        Post, 
        related_name="recipe",
        verbose_name="Пост",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    class Meta:
        verbose_name = "рецепт"
        verbose_name_plural = "рецепты"
        
    def __str__(self):
        if len(self.name) > 15:
            return f"{self.name[:15]}..."
        else:
            return self.name
    
    
class Comment(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=50)
    email  = models.CharField(max_length=100)
    website = models.CharField(verbose_name="Веб-сайт", max_length=150, blank=True)
    message = models.TextField(verbose_name="Комментарий", max_length=500)
    post = models.ForeignKey(Post, related_name="comment", verbose_name="Пост", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "комментарии"
    
    def __str__(self):
        if len(self.name) > 15:
            return f"{self.name[:15]}..."
        else:
            return self.name