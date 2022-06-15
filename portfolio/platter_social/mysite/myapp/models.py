from django.db import models
from users.models import Profile

# Create your models here.


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255)


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class PostRecipe(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)
    recipe_image = models.ImageField()
    title = models.CharField(max_length=150)
    recipe_yield = models.CharField(max_length=50)
    prep_time = models.CharField(max_length=50)
    cook_time = models.CharField(max_length=50)
    total_time = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=1000)
    directions = models.TextField(max_length=1000)


class CookBookRecipe(models.Model):
    cook_book = models.ForeignKey(Profile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(PostRecipe, on_delete=models.CASCADE)
