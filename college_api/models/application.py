from django.db import models
from django.contrib.auth import get_user_model

# Create your College Application Models.
# When a User is removed from the database so are the Applications associated with it.
# Fields - Name of the Application, Url link to the application,  when the application was created,
#  and the User associated with the application.
class Application(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  link = models.URLField()
  created = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The application named '{self.name}' was created {self.created} by {self.owner.email}"

  def as_dict(self):
    """Returns dictionary version of Application models"""
    return {
        'id': self.id,
        'name': self.name,
        'link': self.link,
        'created': self.created
    }
