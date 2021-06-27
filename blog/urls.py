from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogindex, name="blogindex"),
    path('<uuid:pk>',views.blog_detail, name='blog_detail'),
    path("<category>/", views.blog_category, name="blog_category"),
]
