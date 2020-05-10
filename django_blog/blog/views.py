from django.shortcuts import render

posts = [
    {
        'author': 'Bob',
        'title': 'Blog Post 1',
        'content': 'quality content here',
        'date': 'August 28, 2020'
    },
    {
        'author': 'Jack',
        'title': 'Blog Post 2',
        'content': 'quality content here',
        'date': 'August 30, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
