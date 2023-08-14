from django.urls import path
from .views import UserCreateView, PostCreateView, PostDetailView, LikeCreateView
from .views import UserRegistrationView, BulkPostDeleteView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('posts/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', LikeCreateView.as_view(), name='like-create'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('posts/bulk_delete/', BulkPostDeleteView.as_view(),
         name='bulk-post-delete'),
]
