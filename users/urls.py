from django.urls import path
from .views import RegisterView, LoginView, LogoutView, FollowOpView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_url'),
    path('login/', LoginView.as_view(), name="login_url"),
    path('logout/', LogoutView, name="logout_url"),
    path('follow/<int:id>', FollowOpView, name="follow_url"),
    path('profile/<str:username>', ProfileView.as_view(), name="profile_url")
]
