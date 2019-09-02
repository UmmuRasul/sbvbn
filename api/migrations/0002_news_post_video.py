# Generated by Django 2.2.4 on 2019-09-02 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('categories', models.CharField(choices=[('Health', 'health'), ('Skills', 'skills'), ('Sports', 'sports'), ('Politics', 'politics'), ('Social', 'social'), ('Motivateion', 'motivation'), ('Business', 'business'), ('Entertainment', 'entertainment')], default='Education', max_length=40)),
                ('content', models.FileField(upload_to='profile_pics', verbose_name='content')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('comments', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('categories', models.CharField(choices=[('Health', 'health'), ('Skills', 'skills'), ('Sports', 'sports'), ('Politics', 'politics'), ('Social', 'social'), ('Motivateion', 'motivation'), ('Business', 'business'), ('Entertainment', 'entertainment')], default='Education', max_length=40)),
                ('image', models.ImageField(upload_to='profile_pics')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
