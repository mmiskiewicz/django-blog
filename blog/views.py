from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def posts(request):
    return render(request, "blog/posts.html")


def post(request, post_id):
    return render(request, "blog/post.html", {
        "post_id": post_id,
    })
