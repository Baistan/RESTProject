from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/',blogCreate,name='blog-create'),
    path('update/<int:pk>/',blogUpdate,name='blog-update'),
    path('delete/<int:pk>/',blogDelete,name='blog-delete'),
    path('blog-list/',blogList,name='blog-list'),
    path('post-view/<int:pk>/',postView,name='post-view'),
    path('post-view/<int:blog_id>/post-update/<int:post_id>/',postUpdate,name='post-update'),
    path('post-view/<int:blog_id>/post-delete/<int:post_id>/',postDelete,name='post-delete'),
    path('post-list/',postList,name='post-list'),


]

