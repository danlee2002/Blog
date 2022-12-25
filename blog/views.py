from django.shortcuts import render
# Create your views here.
posts = [
    {'author': 'Daniel Lee',
    'title' :  'Blog post 1',
    'content' : 'First post content',
    'date_posted' : 'August 28, 2022'},
     {'author': 'Daniel Lee',
    'title' :  'Blog post 1',
    'content' : 'First post content',
    'date_posted' : 'December 25, 2022'}
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)
def about(request, ):
    return render(request, 'blog/about.html', {'title': 'About'})
