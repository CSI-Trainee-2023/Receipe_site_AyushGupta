from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User 
# Create your views here.

def index(request):
    if request.method=="POST":
        data=request.POST
        Recipe.objects.create(
            name=data.get('name'),
            description=data.get('description'),
            user=request.user
        )
        return redirect('homepage')
    return render(request,'index.html')


def home(request):
    receipe_list=Recipe.objects.order_by("-id")
    if request.GET.get('search'):
        receipe_list=receipe_list.filter(name__icontains= request.GET.get('search'))
    context={'recipe':receipe_list}
    return render(request,'home.html',context)


def myrecipes(request):
    receipe_list=Recipe.objects.filter(user=request.user)
    if request.GET.get('search'):
        receipe_list=receipe_list.filter(name__icontains= request.GET.get('search'))

    context={'recipe':receipe_list}
    return render(request,'myrecipes.html',context)


def delete_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('myrecipes')

def update_recipe(request,id):
    queryset=Recipe.objects.get(id=id)
    description=queryset.description
    name=queryset.name

    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        description=data.get('description')
        queryset.description=description
        queryset.name=name
        queryset.save()
        return redirect('myrecipes')
    context={'recipe':queryset}
    return render(request,'update_recipe.html',context)

def detail_recipe(request,id):
    receipe_list=Recipe.objects.get(id=id)
    context={'recipe':receipe_list}
    return render(request,'recipe_detail.html',context)