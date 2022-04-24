from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from .trackcollege import TrackCollege

# Create your College Model.
# Each college is represented by set fields that do not change.   Name, city and state
# including a college image/logo and also all application deadline dates for early_desicion,
# early_action and regular action.  Included is the home page where the application link
# is.
class College(models.Model):
  name = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=32)
  image = models.URLField()
  early_decision = models.DateField()
  early_action = models.DateField()
  regular_decision = models.DateField()
  app_home_link = models.URLField()

  track_colleges = models.ManyToManyField(
      settings.AUTH_USER_MODEL,
      through=TrackCollege,
      through_fields=('college', 'owner')
  )

  def __str__(self):
    # This must return a string
    return f"{self.name} {self.city},{self.state}"

  def as_dict(self):
    """Returns dictionary version of Colelge model"""
    return {
        'id': self.id,
        'name': self.name,
        'city': self.city,
        'state': self.state,
        'image': self.image,
        'early_decision': self.early_decision,
        'early_action': self.early_action,
        'regular_decision': self.regular_decision,
        'app_home_link': self.app_home_link
    }
