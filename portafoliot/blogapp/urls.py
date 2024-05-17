from django.urls import path
from blogapp import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
]
