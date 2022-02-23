from turtle import title
from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.response import Response


class PostUserWritePermission(BasePermission):
    message = 'Editing post is restriced to the author only.'
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        print(item)
        if self.basename is 'postbycategory':
            return get_object_or_404(Post, category=item)

        return get_object_or_404(Post, slug=item)
    
    #Define custom queryset
    def get_queryset(self):
        return Post.objects.all()


class CategoryList(viewsets.ViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    
    def list(self, request):
        serializer_class = CategorySerializer(self.queryset, many=True)
        return Response(serializer_class.data)    


""" class PostList(viewsets.ViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.postobjects.all()
    
    def list(self, request):
        serializer_class = PostSerializer(self.queryset, many=True)
        return Response(serializer_class.data)    

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data) """

""" class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer """


""" Concrete View Classes
#CreateAPIView
Used for create-only endpoints.
#ListAPIView
Used for read-only endpoints to represent a collection of model instances.
#RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
#DestroyAPIView
Used for delete-only endpoints for a single model instance.
#UpdateAPIView
Used for update-only endpoints for a single model instance.
##ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
#RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
#RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""