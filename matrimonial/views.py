from django.shortcuts import render
from .models import Profile


def ProfileListView(request):
    profiles=Profile.objects.all()
    return render (request,'matrimonial/profile_list.html' ,{'profiles':profiles})

def ProfileDetailView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render (request, 'matrimonial/profile_detail.html' ,{'profile':profile})