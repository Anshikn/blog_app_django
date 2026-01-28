from django.urls import path, include
from .views import blog_index,delete_blog,edit_blog

urlpatterns = [
    path('', blog_index, name='blog_index'),
    path('delete/<int:blog_id>/', delete_blog, name='delete_blog'),
    path('edit/<int:blog_id>/', edit_blog, name='edit_blog'),
    
]
    