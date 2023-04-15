from django.shortcuts import render
from datetime import date

# Create your views here.

posts_list = [
    {
        "title": "Spring",
        "slug": "spring",
        "subtitle": "It's getting warmer and warmer!",
        "text": """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore 
        magna aliqua. Eleifend quam adipiscing vitae proin sagittis nisl rhoncus mattis. Vel quam elementum pulvinar 
        etiam non quam lacus suspendisse. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat. 
        Malesuada pellentesque elit eget gravida cum sociis natoque penatibus. Massa sed elementum tempus egestas sed 
        sed risus. Aenean pharetra magna ac placerat vestibulum lectus mauris. Elementum nisi quis eleifend quam 
        adipiscing vitae proin sagittis. Ultricies tristique nulla aliquet enim tortor at auctor. Sit amet purus gravida
         quis blandit. Ut faucibus pulvinar elementum integer enim neque volutpat.

        Interdum velit euismod in pellentesque massa. Vitae auctor eu augue ut lectus arcu bibendum at. Donec massa 
        sapien faucibus et molestie ac. Integer quis auctor elit sed vulputate. Volutpat diam ut venenatis tellus in 
        metus. Ornare arcu dui vivamus arcu felis bibendum ut tristique. Nulla porttitor massa id neque aliquam 
        vestibulum morbi blandit cursus. Aliquet lectus proin nibh nisl condimentum. Non curabitur gravida arcu ac 
        tortor. Massa eget egestas purus viverra accumsan. Eget mauris pharetra et ultrices neque ornare aenean euismod 
        elementum. Turpis in eu mi bibendum neque. Nulla porttitor massa id neque aliquam vestibulum morbi blandit 
        cursus. Facilisi cras fermentum odio eu feugiat pretium nibh ipsum consequat.
        """,
        "author": "Matt",
        "image": "https://images.unsplash.com/photo-1448375240586-882707db888b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9yZXN0fGVufDB8fDB8fA%3D%3D&w=1000&q=80",
        "date": date(2023, 12, 11),
    }
]


def index(request):
    return render(request, "blog/index.html", {
        "posts": posts_list,
    })


def posts(request):
    return render(request, "blog/posts.html")


def post(request, slug):
    identified_post = next(post for post in posts_list if post["slug"] == slug)
    return render(request, "blog/post.html", {
        "post": identified_post,
    })

