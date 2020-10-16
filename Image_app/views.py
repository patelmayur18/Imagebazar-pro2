from django.shortcuts import render
from .models import Category,Image
# Create your views here.
def home(request):
    cats = Category.objects.all()
    image = Image.objects.all()
    context = {
        'cats':cats,
        'image':image,
    }
    return render(request,'index.html',context)
def Select_image(request,cid):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    image = Image.objects.filter(cat=category)
    context = {
        'cats':cats,
        'image':image
    }
    return render(request,'index.html',context)