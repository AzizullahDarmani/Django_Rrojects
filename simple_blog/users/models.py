from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    bio = models.TextField()
    profile_pciture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    

    def __str__(self):
        return f"{self.user.username}'s profile"
    
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers'  )

    def __str__ (self):
        return f"{self.follower.username} follows {self.following.username}"