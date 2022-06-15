from .models import Post, PostImage, PostComment, PostLike
from django.shortcuts import redirect
from django.contrib import messages


def detail_view(request, posts):
    images = list()
    comments = list()
    like_counts = list()
    likes = list()

    for post in posts:
        post_images = PostImage.objects.filter(post=post)
        post_comments = PostComment.objects.filter(post=post)
        post_likes = PostLike.objects.filter(post=post).count()
        liked = PostLike.objects.filter(post=post, profile=request.user.profile).exists()
        images.append(post_images)
        comments.append(post_comments)
        like_counts.append(post_likes)
        likes.append(liked)

    images.reverse()
    comments.reverse()
    like_counts.reverse()
    likes.reverse()

    return images, comments, like_counts, likes


def list_view(request, posts):
    post_images = list()

    for post in posts:
        image = PostImage.objects.filter(post=post).first().image.url
        post_images.append(image)

    post_images.reverse()

    return post_images


def check_comment_change(request):
    if 'commentPost' in request.POST:
        comment = PostComment()
        post_id = request.POST.get('commentPost')
        comment.post = Post.objects.get(id=post_id)
        comment.profile = request.user.profile
        comment.comment = request.POST.get('commentText')
        comment.save()

    elif 'deleteComment' in request.POST:
        commentID = request.POST.get('deleteComment')
        comment = PostComment.objects.get(id=commentID)
        if comment.profile == request.user.profile or comment.post.profile == request.user.profile:
            comment.delete()


def check_like(request):
    if 'likePost' in request.POST:
        post_id = request.POST.get('likePost')
        post = Post.objects.get(id=post_id)
        profile = request.user.profile

        try:
            like = PostLike.objects.get(post=post, profile=profile)
            like.delete()
        except PostLike.DoesNotExist:
            like = PostLike(post=post, profile=profile)
            like.save()
