from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/home.html', {'all_posts':all_posts})
