from django.urls import path
from .views import (
    PostCreateView,
    ApprovePostView,
    PostUpdateView,
    PostDeleteView,
    PostPendingListView,
    PostApprovedListView
)

urlpatterns = [
    path('posts/pending/', PostPendingListView.as_view()),
    path("posts/approved/", PostApprovedListView.as_view()),
    path('posts/', PostCreateView.as_view()),
    path('posts/<str:post_id>/approve/', ApprovePostView.as_view()),
    path('posts/<str:post_id>/', PostUpdateView.as_view()),
    path('posts/<str:post_id>/delete/', PostDeleteView.as_view()),
]