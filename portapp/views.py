from django.shortcuts import render
from . models import Image,Tag



# Create your views here.
def index(request):
    images = Image.objects.all()
    tag = Tag.objects.all()
    return render(request, 'index.html',{'images': images[::-1], 'tag':tag})

