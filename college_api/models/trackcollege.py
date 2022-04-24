from django.db import models
from django.contrib.auth import get_user_model

# TrackCollege is the table used to track the Many User to Many College relationship
# A user may be interested in Many Colleges.  A College may have many Users interested
# in it.  This table allows us to add specific fields for that relationship like
# tracking the status of that relationship - Interested, Applying or Applied to a college.
class TrackCollege(models.Model):
    TRACK = 'T'
    INTERESTED = 'I'
    APPLYING = 'A'
    APPLIED = 'D'
    CHOICE_STATUS = [
        (TRACK, 'Tracking'),
        (INTERESTED, 'Interested'),
        (APPLYING, 'Applying'),
        (APPLIED, 'Applied')
    ]
    status = models.CharField(
        max_length=1,
        choices=CHOICE_STATUS,
        default=TRACK,
    )

    college = models.ForeignKey('College', on_delete=models.CASCADE, related_name='college_monitored')
    owner = models.ForeignKey( get_user_model(), on_delete=models.CASCADE,
      related_name='college_tracking'
    )

    def __str__(self):
        return f"The colled named '{self.college.name}' is being tracked by {self.owner.email}"

    def as_dict(self):
        return {
            'id': self.id,
            'status': self.status,
            'college_name': self.college.name,
            'user_email': self.owner.email
        }