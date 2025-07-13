from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('update/<int:id>/', views.update_post, name='update_post'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),

    # API endpoints
    path('api/posts/', views.PostListCreateAPI.as_view(), name='api-posts'),
    path('api/posts/<int:pk>/', views.PostRetrieveUpdateDeleteAPI.as_view(), name='api-post-detail'),
]
