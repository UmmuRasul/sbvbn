from django.db import models

# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=60)

     
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password', 'password2']

    def __str__(self):
        return "{}".format(self.email)


