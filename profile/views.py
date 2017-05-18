from django.shortcuts import render


def profile_detail_view(request):
    return render(request, 'profile/user_profile.html')
