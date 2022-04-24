from django.db import models
from django.contrib.auth import get_user_model


# Create your College Tasks Models.
class Task(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=256)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self):
    # This must return a string
    return f"The task named '{self.name}' was created {self.created}"

  def as_dict(self):
    """Returns dictionary version of Task models"""
    return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'created': self.created,
        'updated': self.updated
    }
