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
    # comment=receipe_list.comment_id.all()
    comment=Comments.objects.filter(comment_id=id)
    context={'recipe':receipe_list,'comment':comment}
    return render(request,'recipe_detail.html',context)

def add_comment(request,id):
    if request.method=="POST":
        data=request.POST
        Comments.objects.create(
            comment=data.get('comment'),
            comment_id=Recipe.objects.get(id=id)
        )
        return redirect('detail_recipe',id)
    return render(request,'add_comment.html')
