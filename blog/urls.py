from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.index),
    path("posts/<slug:slug>", views.post, name="post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
