from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Add a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # Add a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

from django.db import models

class BaseInventoryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()

    class Meta:
        abstract = True

class MechanicalPart(BaseInventoryItem):
    material = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    weight = models.FloatField()

class RawMaterial(BaseInventoryItem):
    type = models.CharField(max_length=255)
    purity = models.FloatField()

class ElectricalPart(BaseInventoryItem):
    voltage = models.FloatField()
    current = models.FloatField()
    power_rating = models.FloatField()