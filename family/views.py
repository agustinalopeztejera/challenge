from django.shortcuts import render

from family.models import Family_members

def family_member(request):
    family_member = Family_members.objects.create(name = 'John Smith', age = 50, hobbies = 'jugar al futbol', birthday = 1972)
    context = {
        'family_member':family_member
    }
    return render(request, 'family_member.html', context=context)

def list_family_members(request):
    family_member = Family_members.objects.all()
    context = {
        'family_member':family_member
    }
    return render(request, 'list_family_members.html', context=context) 
