from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class date_course(models.Model):
    date = models.CharField(max_length=11,default='')
    # date of the course
    course_name = models.CharField(max_length=50,default='course0')
    # name of the course
    memo = models.TextField(default='')

    def __str__(self):
        course_str = self.course_name + ':' + self.memo
        return course_str

class userProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='userprofile',
        primary_key=True
    )

    isIntern = models.BooleanField(default=False)
    isJunior = models.BooleanField(default=False)
    isSenior = models.BooleanField(default=False)
    isFamily = models.BooleanField(default=True)
    isMentor = models.BooleanField(default=False)

class attendanceSheet(models.Model):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='attendanceSheet',
        null=True,
        blank=True
    )
    
    course = models.ForeignKey(
        date_course,
        on_delete=models.CASCADE,
        related_name='atdSummary',
        null=True,
        blank=True
    )

    presence = models.BooleanField(default=False)
    absence = models.BooleanField(default=True)
    late = models.BooleanField(default=False)
    personal_leave = models.BooleanField(default=False)

    def status(self):
        if self.presence:
            return 'presence'
        elif self.absence:
            return 'absence'
        elif self.late: 
            return 'late'
        elif self.personal_leave:
            return 'personal leave'
        else:
            return 'fuck you'