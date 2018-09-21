from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post #The dot before models means current directory or current application.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # In case there is no Post with the given pk, it will display much nicer page, the Page Not Found 404 page
    return render(request, 'blog/post_detail.html', {'post': post})