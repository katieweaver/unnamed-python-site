from django.shortcuts import render
from .models import Post

# Create your views here.
#Eventually want this mapping to a dynamic user.
def user_profile(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'art/user_profile.html', context)

