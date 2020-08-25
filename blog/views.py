from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'all_blogs':all_posts})
