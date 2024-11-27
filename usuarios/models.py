from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    id_propio = models.CharField(max_length=50,blank=True, null=True)
    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)