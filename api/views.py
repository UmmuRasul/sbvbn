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



# class PostAPIView(ListAPIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'post.html'

#     def get(self, request):
#         queryset = Post.objects.all()
#         return Response({'posts': queryset})

# class PostAPIView(ListAPIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'news.html'

#     def get(self, request):
#         queryset = Post.objects.all()
#         return Response({'video': queryset})
