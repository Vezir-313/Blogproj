from django.urls import path, include
from . import views

urlpatterns = [
    path("",view=views.blog_list,name="blog_list"), # get -> all blogs
    path("blog/",view=views.blog_form,name="blog_create"), # get post -> insert
    path("blog/update/<int:id>/",view=views.blog_form,name="blog_update"), # get post -> details, update
    path("blog/delete/<int:id>/",view=views.blog_delete,name="blog_delete"), # get -> all blogs
]