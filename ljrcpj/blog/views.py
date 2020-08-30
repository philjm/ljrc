from django.shortcuts import render
from django.utils import timezone
from .models import Post
from cards.models import Cardpost, Stats
from django.views import generic
from bs4 import BeautifulSoup
import requests



def index(request):
    finkle = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    finkles = Cardpost.objects.filter(tag2='mr').order_by('?')
    fank = Cardpost.objects.get(title='Bazooka Comics PSA 10')
    stats = Stats.objects.get(cardcount="95 Cards")
    return render(request, 'blog/index.html', {'finkle': finkle, 'finkles': finkles, 'fank': fank, 'stats': stats})


def card_section(request):
    finkle = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    finkles = Cardpost.objects.all()
    return render(request, 'blog/cardsection.html', {'finkle': finkle, 'finkles': finkles})

def blog(request):
    finkle = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    finkles = Cardpost.objects.filter(tag2='mr').order_by('?')
    return render(request, 'blog/blog.html', {'finkle': finkle, 'finkles': finkles})




def blogdetail(request, slug):
    post = Post.objects.get(slug=slug)
    finkles = Cardpost.objects.filter(tag2='mr').order_by('?')
    finkle = Post.objects.all()
    fink = Post.objects.all()
    return render(request, 'blog/blog-details.html', {'post': post, 'fink': fink, 'finkle': finkle, 'finkles': finkles})

def stats(request):
    post = Stats.objects.all()
    return render(request, 'blog/our_features.html', {'post': post})

def footer(request):
    post = Cardpost.objects.filter(tag2='mr').order_by('?')
    finkle = Post.objects.all()

    return render(request, 'blog/base.html', {'post': post, 'finkle': finkle})
  