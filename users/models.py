from django.db import models
from localflavor.us.models import USZipCodeField
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    zipcode = USZipCodeField(blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

