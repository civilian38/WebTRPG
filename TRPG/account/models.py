from django.contrib.auth.models import AbstractUser
from django.db import models

class TRPGUser(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        if self.nickname:
            return self.nickname
        return self.username