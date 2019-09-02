from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet, api_post_view

router = routers.DefaultRouter()
router.register('users', UserViewSet)

app_name = 'api'


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('<slug>/', api_post_view, name='post')
]