from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.index),
    path("posts/<slug:slug>", views.post, name="post-page"),
    path("favorites", views.favorites, name="favorites"),
]