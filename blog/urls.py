from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("posts", views.posts),
    path("posts/<int:post_id>", views.post),
]
