from django.urls import path
from account.api.views import(
    registartion_view,
)

app_name = 'account'
urlpatterns = [
    path('register/', registartion_view, name='register'),
]
