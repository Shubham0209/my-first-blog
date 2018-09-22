from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post #The dot before models means current directory or current application.
from .forms import PostForm
from django.shortcuts import redirect # to redirect the form to the post_detail page

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # In case there is no Post with the given pk, it will display much nicer page, the Page Not Found 404 page
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST": #check if form already created, if yes then construct the PostForm and go back to the view with all form data we just typed.
        form = PostForm(request.POST) # we're "posting" data just in the HTML file, we have <form> definition had the variable method="POST"
        if form.is_valid(): # check all required fields are set and no incorrect values have been submitted
            post = form.save(commit=False) # commit=False means that we don't want to save the Post model yet – we want to add the author first.
            post.author = request.user
            post.published_date = timezone.now()
            post.save() # preserve changes (adding the author) and a new blog post is created!
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})