from django import forms
from .models import Post, PostComment, PostImage, PostRecipe


# Create your forms here


class PostForm(forms.ModelForm):

    add_recipe = forms.BooleanField(required=False)

    class Meta:
        model = Post
        fields = ['title']


class PostImageForm(forms.ModelForm):

    class Meta:
        model = PostImage
        fields = ['image', 'caption']


class PostRecipeForm(forms.ModelForm):

    class Meta:
        model = PostRecipe
        fields = ['title', 'recipe_image', 'recipe_yield', 'prep_time', 'cook_time', 'total_time', 'ingredients', 'directions']
