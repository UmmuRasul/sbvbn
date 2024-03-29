from rest_framework import  status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.api.serializers import  RegistrationSerializer


@api_view(['POST'])
def registartion_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_vallid():
            account = serializer.save()
            data['response'] = 'successfully registered user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Responce(data)