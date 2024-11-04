# Imported Files and Packages
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Post Status Variable
STATUS = ((0, "Draft"), (1, "Published"))

# Create post
class Post(models.Model):
    """
    Stores a instence of a post entry.
    """
    user = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ["-created_on"]

    def like_counter(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.user} | {self.created_on:%Y-%m-%d %H:%M} | {self.body}"


# Create user profile
class Profile(models.Model):
    """
    Stores an instance of a created user profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    last_active = models.DateTimeField(User, auto_now=True)
    profile_image = CloudinaryField('image', default='placeholder')
    def __str__(self):
        return f"{self.user.username}"

# Create A profile when a user signs-up & automatically follows own profile
@receiver(post_save, sender=User)
def create_user_profile(created, instance, sender, **kwargs):
    if created:
        created_profile = Profile(user=instance)
        created_profile.save()
        created_profile.follows.set([instance.profile.id])
        created_profile.save()