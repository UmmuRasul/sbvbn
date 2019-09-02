from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


CATEGORIES = [
    ('Health','health'),
    ('Skills','skills'),
    ('Sports','sports'),
    ('Politics','politics'),
    ('Social','social'),
    ('Motivateion','motivation'),
    ('Business','business'),
    ('Entertainment','entertainment')

]


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    photo = models.ImageField(upload_to='uploads', blank=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    comments = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100)
    categories = models.CharField(choices=CATEGORIES, default='Education', max_length=40)
    image = models.ImageField(upload_to='profile_pics')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    editor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.categories


class Video(models.Model):
    title = models.CharField(max_length=100)
    categories = models.CharField(choices=CATEGORIES, default='Education', max_length=40)
    content = models.FileField("content", upload_to='profile_pics', max_length=100)
    date = models.DateTimeField(default=timezone.now)
    #['video/x-msvideo', 'application/pdf', 'video/mp4', 'audio/mpeg', ]
    
    def __str__(self):
        return self.title

