from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from api.models import User, Post, News, Video
from rest_framework import status
from api.serializers import UserSerializer, PostSerializer, VideoSerializer, NewSerializer
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


@api_view(['GET'])
def api_post_view(request, slug):

    try:
        post = Post.objects.get(slug=slug)
    except BlogPost.DoesnotExists:
        return Response(status=status.HTTP_404__NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

@api_view(['PUT'])
def api_update_post_view(request, slug):

    try:
        post = Post.objects.get(slug=slug)
    except BlogPost.DoesnotExists:
        return Response(status=status.HTTP_404__NOT_FOUND)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'update was successfully'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_delete_post_view(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except BlogPost.DoesnotExists:
        return Response(status=status.HTTP_404__NOT_FOUND)

    if request.method == 'DELETE':
        operation = post.delete()
        data = {}
        if operation:
            data['success'] = 'delete successfully'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)

@api_view(['POST'])
def api_create_post_view(request, slug):
    account = Account.objects.get(pk=1)
    post =Post(author=account)

    if request.method == 'Post':
        serializers = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)