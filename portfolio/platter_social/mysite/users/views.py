from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import NewUserForm, ProfileForm
from myapp.models import Post, PostImage, PostComment, PostRecipe
from myapp.functions import detail_view, check_comment_change
from .models import Profile, FollowUser
from .functions import is_following

# Create your views here.


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("myapp:follow_feed")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="users/register.html", context={"register_form": form})


@login_required
def profile_page(request, id):
    profile = Profile.objects.get(pk=id)
    following = is_following(request, id)
    posts = Post.objects.filter(profile=profile).order_by('-time')

    search = request.GET.get('searchBox')
    if search != '' and search is not None:
        posts = posts.filter(title__contains=search)

    images, comments, like_counts, likes = detail_view(request, posts)

    if request.method == "POST":
        check_comment_change(request)

    return render(request, 'users/profile.html',
                  {'profile': profile, 'posts': posts, 'following': following, 'images': images, 'comments': comments,
                   'like_counts': like_counts, 'likes': likes})


@login_required
def edit_profile(request):
    instance = request.user.profile
    form = ProfileForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect('profile', request.user.id)

    return render(request, 'users/edit_profile.html', {'form': form})


@login_required
def follow_user(request, id):
    profile = Profile.objects.get(pk=id)
    follow = FollowUser.objects.create(user=request.user, follow=profile)
    follow.save()
    return redirect('profile', id)


@login_required
def unfollow_user(request, id):
    follow = is_following(request, id)
    if follow is not None:
        follow.delete()
    return redirect('profile', id)


