from .models import Profile, FollowUser


def is_following(request, id):
    profile = Profile.objects.get(pk=id)
    try:
        following = FollowUser.objects.get(user=request.user, follow=profile)
    except FollowUser.DoesNotExist:
        following = None
    return following
