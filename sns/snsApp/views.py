from django.shortcuts import render
from .models import Profile

def home_view(request):
    return render(
        request,
        "snsApp/home.html",
        {}
    )
    
def profile_list_view(request):
    profiles = Profile.objects.exclude(user=request.user)
    
    context = {
        "profiles": profiles
    }
    
    return render(
        request,
        "snsApp/profile_list.html",
        context,
    )