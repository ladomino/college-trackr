from django.db import models
from django.contrib.auth import get_user_model
from .college import College
from .collegeapplication import CollegeApplication
from .task import Task
from .applicationtask import ApplicationTask

# Create your College Application Models.
# When a User is removed from the database so are the Applications associated with it.
# Fields - Name of the Application, Url link to the application,  when the application was created,
#  and the User associated with the application.
# When a we get the applications via a user they are known as 'college_applications'
class Application(models.Model):
  name = models.CharField(max_length=100)
  link = models.URLField()
  created = models.DateTimeField(auto_now_add=True)
  
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      related_name='college_application_owners'
  )

  college_applications = models.ManyToManyField(
      College,
      through=CollegeApplication,
      through_fields=('application', 'college')
  )

  application_tasks = models.ManyToManyField(
      Task,
      through=ApplicationTask,
      through_fields=('application', 'task')
  )

  def __str__(self):
    return f"The application named '{self.name}' was created {self.created} by {self.owner.email}"

  def as_dict(self):
    """Returns dictionary version of Application models"""
    return {
        'id': self.id,
        'name': self.name,
        'link': self.link,
        'created': self.created
    }
