from django.shortcuts import render
# Create your views here.
posts = [
    {'author': 'CoreyMs',
    'title' :  'Blog post 1',
    'content' : 'First post content',
    'date_posted' : 'August 28, 2018'},
     {'author': 'CoreyMs',
    'title' :  'Blog post 1',
    'content' : 'First post content',
    'date_posted' : 'August 28, 2018'}
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)
def about(request, ):
    return render(request, 'blog/about.html', {'title': 'About'})
