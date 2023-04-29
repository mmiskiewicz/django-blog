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
    stored_posts = request.session.get("stored_posts")
    if stored_posts is not None:
        is_marked_as_favorite = identified_post.id in stored_posts
    else:
        is_marked_as_favorite = False
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
        "is_marked_as_favorite": is_marked_as_favorite,
    })


def favorites(request):
    stored_posts = request.session.get("stored_posts")
    context = {}

    if stored_posts is None or len(stored_posts) == 0:
        stored_posts = []
        posts = None
    else:
        posts = Post.objects.filter(id__in=stored_posts)
        p = Paginator(posts, 3)
        page = request.GET.get("page")
        posts = p.get_page(page)


    if request.method == "POST":

        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")

    return render(request, "blog/favorite-posts.html", {
        "context": context,
        "posts": posts,
    })
