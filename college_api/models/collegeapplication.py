from django.db import models

# The CollegeApplication Model represents the Many to Many relation of Colleges to Applications.
# An Application can be sent to many Colleges and a College can have Many Applications.
# For a given Application to a College each has a unique date submitted and progress and
# decision deadline they have applied to.
class CollegeApplication(models.Model):
    date_submitted = models.DateField()
    in_progress = models.BooleanField()
    hold = models.BooleanField()
    early_decision = models.BooleanField()
    early_action = models.BooleanField()
    regular_decision = models.BooleanField()
    college = models.ForeignKey('College', on_delete=models.CASCADE)
    application = models.ForeignKey('Application', on_delete=models.CASCADE)

    def __str__(self):
        return f"Application named {self.application.name} submitted {self.date_submitted} for {self.name}"

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
