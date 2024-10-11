
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm  # Import the forms
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})



@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            return redirect('post_list')  # Redirect to the post list after saving
    else:
        form = PostForm()

    return render(request, 'post_form.html', {'form': form})










def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'post_form.html', {'form': form, 'post': post})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request, 'post_confirm_delete.html', {'post': post})








# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)  # Get the post or return a 404 if not found
#     comments = post.comments.all()  # Assuming you have a related name for comments

#     if request.method == 'POST' and request.user.is_authenticated:
#         form = CommentForm(request.POST)  # Create a new comment form instance
#         if form.is_valid():
#             comment = form.save(commit=False)  # Don't save it yet
#             comment.post = post  # Link comment to the post
#             comment.author = request.user  # Set the comment author
#             comment.save()  # Save the comment
#             return redirect('post_detail', id=post.id)  # Redirect to the same post detail view
#     else:
#         form = CommentForm()  # Create a blank comment form for GET requests

#     return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form})
