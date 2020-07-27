from django.urls import path, re_path
from . import views as view

urlpatterns = [
    path('', view.show_all_blog, name="show_all_blog"),
    path('<slug:slug_text>', view.show_blog, name="show_blog")
]
