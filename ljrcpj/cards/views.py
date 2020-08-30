from django.shortcuts import render
from django.utils import timezone
from .models import Cardpost
from blog.models import Post
import requests

def post_list(request):
    fink = Post.objects.all()
    finkle = Cardpost.objects.all()
    return render(request, 'cards/card-details.html', {'finkle': finkle})

def card_section(request):
    finkles = Cardpost.objects.all()
    return render(request, 'cards/cardsection.html', {'fink': fink})

def card(request, slug):
    post = Cardpost.objects.get(slug=slug)
    fink = Cardpost.objects.all().order_by('?')
    psa10 = Cardpost.objects.filter(tag1='PSA 10')
    finkles = Cardpost.objects.filter(tag2='mr').order_by('?')
    finkle = Post.objects.all()
    return render(request, 'cards/card-details.html', {'post': post, 'fink': fink, 'finkle': finkle, 'finkles': finkles})

def cardsall(request):
    finkles = Cardpost.objects.filter(tag2='mr').order_by('?')
    finkle = Post.objects.all()
    post = Cardpost.objects.all()
    psa10 = Cardpost.objects.filter(tag1='PSA 10')
    psa9 = Cardpost.objects.filter(tag1='PSA 9')
    psa8 = Cardpost.objects.filter(tag1='PSA 8')
    bgs10 = Cardpost.objects.filter(tag1='BGS 10')
    bgs95 = Cardpost.objects.filter(tag1='BGS 9.5')
    bgs9 = Cardpost.objects.filter(tag1='BGS 9')
    raw = Cardpost.objects.filter(tag1='Raw')
    return render(request, 'cards/cardsall.html', {'finkle': finkle, 'finkles': finkles, 'post': post, 'psa10': psa10, 'psa9': psa9, 'psa8': psa8, 'bgs10': bgs10, 'bgs95': bgs95, 'bgs9': bgs9, 'raw': raw})

def cardscar(request):
    fink = Cardpost.objects.all()
    return render(request, 'cards/cardscar.html', {'fink': fink})

def fank(request):
    fank = Cardpost.objects.filter(tag2='mr').order_by('?')
    return render(request, 'blog/chooseus.html', {'fank': fank})

