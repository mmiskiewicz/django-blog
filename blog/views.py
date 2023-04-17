from django.shortcuts import render, get_object_or_404
from datetime import date
from .models import Post, Tag, Author

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/index.html", {
        "posts": posts,
    })


def posts(request):
    return render(request, "blog/posts.html")


def post(request, slug):
    # identified_post = next(post for post in posts_list if post["slug"] == slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {
        "post": identified_post,
    })
