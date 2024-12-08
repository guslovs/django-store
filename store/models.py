from django.db import models

# Create your models here.

class TagModel(models.Model):
    caption = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.caption}"

class LoginModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f"{self.name}"
    
class ArticleModel(models.Model):
    name = models.CharField(max_length=50, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="posts", null=True)
    description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, null=True)
    tag = models.ManyToManyField(TagModel)
    
    def __str__(self):
        return f"{self.name}"