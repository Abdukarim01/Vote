from django.shortcuts import render
from .models import Category,Places

def home(request):
    category = Category.objects.all()
    places = Places.objects.select_related("bind").all()
    context = {
        "lists":category,
        "lis2":places
    }

    return render(request,'index/index.html',context)