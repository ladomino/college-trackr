from django.db import models

# The CollegeApplication Model represents the Many to Many relation of Colleges to Applications.
# An Application can be sent to many Colleges and a College can have Many Applications.
# For a given Application to a College each has a unique date submitted and progress and
# decision deadline they have applied to.
class CollegeApplication(models.Model):
    date_submitted = models.DateField(auto_now=True)
    in_progress = models.BooleanField(default=True)
    hold = models.BooleanField(default=False)
    early_decision = models.BooleanField(default=False)
    early_action = models.BooleanField(default=False)
    regular_decision = models.BooleanField(default=True)
    college = models.ForeignKey('College', on_delete=models.CASCADE, related_name='college_picked')
    application = models.ForeignKey('Application', on_delete=models.CASCADE, related_name='college_app')

    def __str__(self):
        return f"Application named {self.application.name} submitted {self.date_submitted} for {self.application.owner.email}"

    def as_dict(self):
        """Returns dictionary version of Application models"""
        return {
            'id': self.id,
            'date_submitted': self.date_submitted,
            'in_progress' : self.in_progress,
            'hold' : self.hold,
            'early_decision': self.early_decision,
            'regular_decision': self.regular_decision,
            'college_name' : self.college.name,
            'application_name' : self.application.name
        }
