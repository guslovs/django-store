from django.contrib import admin
from store.models import LoginModel, ArticleModel, TagModel

# Register your models here.

admin.site.register(LoginModel)
admin.site.register(ArticleModel)
admin.site.register(TagModel)