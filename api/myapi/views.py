from rest_framework.generics import ListAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import User, Post, News, Video
from rest_framework import status
from api.myapi.serializers import PostSerializer, VideoSerializer, NewSerializer


@api_view(['GET'])
def api_post_view(request):

    try:
        post = Post.objects.get()
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404__NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

@api_view(['PUT'])
def api_update_post_view(request):

    try:
        post = Post.objects.get()
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
def api_delete_post_view(request):
    try:
        post = Post.objects.get()
    except BlogPost.DoesNotExist:
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
def api_create_post_view(request):
    account = Account.objects.get(pk=1)
    post =Post(author=account)

    if request.method == 'Post':
        serializers = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)