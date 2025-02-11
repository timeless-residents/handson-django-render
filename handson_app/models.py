from django.db import models
from django.db.models.manager import Manager

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Add type hint for objects
    objects: Manager = models.Manager()

    def __str__(self) -> str:
        return str(self.name)