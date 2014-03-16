from django.shortcuts import render, get_object_or_404
from account.models import UserProfile

def all_users(request):
    user_list = UserProfile.objects.filter(is_staff=False)
    context = { 'user_list': user_list }
    return render(request, 'account/all_users.html', context)

def detail(request, user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    return render(request, 'account/user_detail.html', { 'user': user })