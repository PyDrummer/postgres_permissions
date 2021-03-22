from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from my_app.permissions import IsOwnerOrReadOnly
from .models import Blog
from .serializer import BlogSerializer 


# Create your views here.

class BlogList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
