from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('profile/<str:uname>/', user_dashboard, name="user_dashboard"),
    path('deleteBlog/', deleteBlog, name="deleteBlog"),
    path('submitForReviewBlog/', submitForReviewBlog, name="submitForReviewBlog"),
    path('editBlog/', editBlog, name="editBlog"),
    path('contact/', contact, name="contact"),
]
