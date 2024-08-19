from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False, # followers can have multiple followers and so on
        blank=True, # allows user to have no following/followers
    )
    
    date_modified = models.DateTimeField(User, auto_now=True)
    
    def __str__(self):
        return self.user.username
    
# everytime the user hit save, this block of code will run
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        
        user_profile.follows.set(
            [instance.profile.id]
        )
        user_profile.save()

# hook the create_profile to the post_save
post_save.connect(create_profile, sender=User)