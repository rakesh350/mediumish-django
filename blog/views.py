from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post

# Create your views here.
def home(request):
    all_posts = get_list_or_404(Post.objects.order_by('-id'))
    return render(request, 'blog/home.html', {'all_posts':all_posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/details.html', {'post_detail' : post_detail})