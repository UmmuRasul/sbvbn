from django.urls import path, include
from rest_framework import routers
from api.myapi.views import(
    
    api_post_view,
    api_update_post_view,
    api_delete_post_view,
    api_create_post_view
) 


app_name = 'api'


urlpatterns = [
    path('post/', api_post_view, name='post'),
    path('post/update/', api_update_post_view, name='update'),
    path('post/delete/', api_delete_post_view, name='delete'),
    path('create/', api_create_post_view, name='create')
]

