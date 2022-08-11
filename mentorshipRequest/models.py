import uuid
from django.db import models
from jsonfield import JSONField
# Create your models here.
class MentorshipRequest(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(verbose_name='Title', unique=True, max_length=16, blank=False)
    requestDescription = models.TextField(verbose_name="Description",max_length=512, blank=True) 
    duration = models.CharField(verbose_name='Duration', unique=True, max_length=16, blank=False) 
    location = models.CharField(verbose_name='Location', unique=True, max_length=16, blank=False) 
    lookingFor = JSONField(verbose_name='Looking for help with',default=list,null=True,blank=True)
    Requirements =  JSONField(verbose_name='Requirements',default=list,null=True,blank=True)
    background = JSONField(verbose_name='background',default=list,null=True,blank=True)
    experience = models.CharField(verbose_name='experience', unique=True, max_length=16, blank=False) 
    # mentor = models.ForeignKey('mentor.Mentor', on_delete=models.CASCADE,
    #                            related_name='mentor_mentorships')  # TODO Give better and smaller related_name
    # mentee = models.ForeignKey('mentee.Mentee', on_delete=models.CASCADE, related_name='request_description')
    # status = models.IntegerField(choices=MentorshipStatus.choices, default=MentorshipStatus.ONGOING)
    # start_date = models.DateField(verbose_name='Start date', auto_now_add=True)
    # end_date = models.DateField(verbose_name='End date', blank=True,
                                # null=True)  # When the mentor-mentee relationship actually ended
    # expected_end_date = models.DateField(verbose_name='Expected end date', null=True)
    is_paid = models.BooleanField(verbose_name='Is paid?', default=False, blank=True)
    amount = models.IntegerField(verbose_name='amount', blank=True, default=False)

    def __str__(self):
        return '{}(mentor={}, mentee={})'.format(self.__class__.__name__,
                                                 self.mentor.user.email,
                                                 self.mentee.user.email)