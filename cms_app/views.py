from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import User, Post, Like
from .serializers import UserSerializer, PostSerializer, LikeSerializer, UserRegistrationSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerForPrivate, PublicReadAccess, PrivateOwnerAccess
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import PublicReadAccess, PrivateOwnerAccess


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({'access_token': access_token}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          (PublicReadAccess | PrivateOwnerAccess)]


class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)


class BulkPostDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        # Delete all posts
        Post.objects.all().delete()
        return Response({"detail": "All posts deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
