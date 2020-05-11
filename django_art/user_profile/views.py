from django.shortcuts import render

# Create your views here.
#Eventually want this mapping to a dynamic user.
def user_profile(request):
    return render(request, 'user_profile/user_profile.html')