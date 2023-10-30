from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    if request.method=="POST":
        data=request.POST
        Recipe.objects.create(
            name=data.get('name'),
            description=data.get('description')
        )
        return redirect('/Recipe/')
    return render(request,'index.html')