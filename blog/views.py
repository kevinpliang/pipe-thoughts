from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Kevin',
        'title': 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'March 13, 2021'
    },
    {
        'author': 'Rahil',
        'title': 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'March 14, 2021'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})