from django.urls import path

from theblog.models import Category
from .views import AddPostView, HomeView, ArticleDetailView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name = "add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name = "update-post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name = "delete-post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name="like_post"),
]

