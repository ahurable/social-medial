from django.urls import path
from .views import AddPostView, PostDetailView, LikeView, search_results, CommentView

urlpatterns = [
    path('add/', AddPostView.as_view(), name="add_post_url"),
    path('<int:id>', PostDetailView, name="postd_url"),
    path('like/<int:id>', LikeView, name="post_like_url"),
    path('search/', search_results, name="search_results"),
    path('comment/<int:id>', CommentView.as_view(), name="comment_url")
]