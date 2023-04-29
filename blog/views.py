from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator
from .forms import CommentForm
from django.views import View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse

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
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = identified_post
            comment.save()
            return HttpResponseRedirect(reverse("post-page", args=[slug]))
    return render(request, "blog/post.html", {
        "post": identified_post,
        "form": form,
        "comments": identified_post.comments.all().order_by("-id"),
    })
