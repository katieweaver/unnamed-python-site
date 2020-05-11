from django.shortcuts import render

# Create your views here.
#Eventually want this mapping to a dynamic user.
def profile(request):
    return render(request, 'profile/profile.html')