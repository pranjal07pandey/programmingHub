from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_subscribed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(blank=False)
    username = models.CharField(max_length=100, blank=False)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    thumbnail_url = models.CharField(max_length=1000)
    video_url = models.CharField(max_length=1000)
    c_types = (
        ('free', 'free' ),
        ('paid', 'paid'),
    )
    course_type = models.CharField(max_length=100, choices=c_types)

    course_length= models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=500)
    video_url = models.CharField(max_length=500)
    l_types =(
        ('free', 'free'),
        ('paid', 'paid')
    )
    lesson_type = models.CharField(max_length=100, choices=l_types, default='paid')

    def __str__(self):
        return self.title