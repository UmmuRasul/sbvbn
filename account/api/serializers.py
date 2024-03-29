from rest_framework import serializers
from account.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(max_length=100,write_only=True)

    class Meta:
        model = Account
        fields = ['email','username','password','password2']
        extra_kwargs = {
            'passmword': {'write_only': True}
        }

    def save(self):
        account = Account(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'password dont match.'})
            account.set_password(passmword)
            account.save()
            return account
