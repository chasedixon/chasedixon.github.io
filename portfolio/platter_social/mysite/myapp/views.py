from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PostForm, PostRecipeForm
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import Post, PostImage, PostRecipe, CookBookRecipe
from django.contrib.auth.models import User
from users.models import FollowUser
from .functions import detail_view, list_view, check_comment_change, check_like

# Create your views here.


@login_required
def follow_feed(request):
    following = FollowUser.objects.filter(user=request.user)
    profile_list = list()
    for follow in following:
        profile_list.append(follow.follow)
    posts = Post.objects.filter(profile__in=profile_list).order_by('-time', '-id')

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    images, comments, like_counts, likes = detail_view(request, posts)

    if request.method == "POST":
        check_comment_change(request)
        check_like(request)

    return render(request, 'myapp/follow_feed.html',
                  {'posts': posts, 'images': images, 'comments': comments, 'like_counts': like_counts, 'likes': likes})


@login_required
def add_post(request):
    ImageFormset = inlineformset_factory(Post, PostImage, fields='__all__', extra=5, can_delete=False)

    post_form = PostForm(request.POST or None)
    image_formset = ImageFormset(request.POST or None, request.FILES or None)

    for form in image_formset:
        form.fields['caption'].required = False
    
    if post_form.is_valid() and image_formset.is_valid():
        print('Saving forms')
        post = post_form.save(commit=False)
        post.profile = request.user.profile
        post.save()
        print('post saved: ' + post.title)
        for form in image_formset.forms:
            if form.cleaned_data.get('image'):
                image = form.save(commit=False)
                image.post = post
                image.save()
        messages.success(request, f'Dish Served!')
        if post_form.cleaned_data.get('add_recipe'):
            return redirect('myapp:add_recipe', post.id)
        return redirect('myapp:follow_feed')

    return render(request, 'myapp/add_post.html', {'post_form': post_form, 'image_formset': image_formset})


@login_required
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
        if request.user == post.profile.user:
            post.delete()
            messages.success(request, f'Post deleted')
            return redirect('profile', request.user.id)

        messages.error(request, f'Error deleting post. Check user login.', extra_tags=' alert-danger')
    except Post.DoesNotExist:
        messages.error(request, 'Error deleting post. Post not found.', extra_tags=' alert-danger')
    return redirect('profile', request.user.id)


@login_required
def add_recipe(request, id):
    post = Post.objects.get(id=id)
    form = PostRecipeForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.post = post
        recipe.save()
        messages.success(request, f'Added Recipe for ' + post.title)
        return redirect('myapp:follow_feed')

    return render(request, 'myapp/add_recipe.html', {'post': post, 'form': form})


@login_required
def view_recipe(request, id):
    post = Post.objects.get(id=id)
    recipe = PostRecipe.objects.get(post=post)
    ingredients = recipe.ingredients.split('\n')
    directions = recipe.directions.split('\n')
    recipe_in_book = CookBookRecipe.objects.filter(cook_book=request.user.profile, recipe=recipe).exists()

    if request.GET:
        return render(request, 'myapp/print_recipe.html',
                      {'recipe': recipe, 'ingredients': ingredients, 'directions': directions})
    if request.POST:
        try:
            recipe = CookBookRecipe.objects.get(cook_book=request.user.profile, recipe=recipe)
            recipe.delete()

        except CookBookRecipe.DoesNotExist:
            recipe = CookBookRecipe(cook_book=request.user.profile, recipe=recipe)
            recipe.save()

        return redirect('myapp:view_recipe', id)

    return render(request, 'myapp/view_recipe.html',
                  {'recipe': recipe, 'recipe_in_book': recipe_in_book, 'ingredients': ingredients,
                   'directions': directions})


@login_required
def recipe_book(request):
    recipes = CookBookRecipe.objects.filter(cook_book=request.user.profile)

    return render(request, 'myapp/recipe_book.html', {'recipes': recipes})


@login_required
def discover(request):
    posts = Post.objects.exclude(profile=request.user.profile).order_by('-time', '-id')

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    post_images = list_view(request, posts)

    return render(request, 'myapp/discover.html', {'posts': posts, 'post_images': post_images})



@login_required
def search_results(request):
    query = request.GET.get('searchBox')
    profiles = User.objects.filter(username__icontains=query) | User.objects.filter(profile__city__icontains=query)
    posts = Post.objects.filter(title__icontains=query).order_by('-time', '-id')

    post_images = list_view(request, posts)

    return render(request, 'myapp/search_results.html',
                  {'profiles': profiles, 'posts': posts, 'post_images': post_images})
