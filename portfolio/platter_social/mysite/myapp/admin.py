from django.contrib import admin
from .models import Post, PostComment, PostImage, PostRecipe, PostLike, CookBookRecipe

# Register your models here.
admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(PostImage)
admin.site.register(PostRecipe)
admin.site.register(PostLike)
admin.site.register(CookBookRecipe)
