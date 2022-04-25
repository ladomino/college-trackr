from django.db import models

# The ApplicationTask model is used to track the Many to Many relationship of Many Applications
# can have the same Task as well as Many Tasks can be for one Application.  
# Application Tasks can also have specific due dates and stages of status - like completed or
# working_on.
class ApplicationTask(models.Model):
    YELLOW = 'Y'
    PINK = 'P'
    ORANGE = 'O'
    GREEN = 'G'
    BLUE = 'B'
    RED = 'R'
    TASK_IMPORTANCE = [
        (YELLOW, 'Normal'),
        (PINK, 'Soothing'),
        (ORANGE, 'NeedsAction'),
        (GREEN, 'WorkingOn'),
        (BLUE, 'LookAtMe'),
        (RED, 'AlertNOW'),
    ]
    importance = models.CharField(
        max_length=1,
        choices=TASK_IMPORTANCE,
        default=YELLOW,
    )

    due_date = models.DateField()
    complete = models.BooleanField(default=False)
    working_on = models.BooleanField(default=False)

    application = models.ForeignKey('Application', on_delete=models.CASCADE, related_name='app_tasks')
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='todo')

    def __str__(self):
        return f"Task named {self.task.name} due {self.due_date} for {self.application.name}"

    def is_normal(self):
        return self.importance in {self.YELLOW}

    def is_high_priority(self):
        return self.importance in {self.RED, self.BLUE}

    def is_top_priority(self):
        return self.importance in {self.RED}

    def as_dict(self):
        """Returns dictionary version of Application models"""
        return {
            'id': self.id,
            'importance': self.importance,
            'due_date' : self.due_date,
            'complete' : self.complete,
            'working_on': self.working_on,
            'application_name' : self.application.name,
            'task_name': self.task.name
        }
