from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by("-date")

    p = Paginator(Post.objects.all(), 3)
    page = request.GET.get("page")
    posts_list = p.get_page(page)

    return render(request, "blog/index.html", {
        "posts": posts,
        "posts_list": posts_list,
    })


def posts(request):
    return render(request, "blog/posts.html")


def post(request, slug):
    # identified_post = next(post for post in posts_list if post["slug"] == slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post.html", {
        "post": identified_post,
    })
