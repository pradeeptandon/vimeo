from django.db import models

class user_data(models.Model):
    username = models.CharField(max_length = 100)
    url = models.URLField()
    payment = models.CharField(max_length = 10)
    videos = models.CharField(max_length = 10)
    staff_pick = models.CharField(max_length = 10)

    class Meta:
        app_label = 'userbase'

    def __unicode__(self):
        return self.username
    
    
class sqf(models.Model):
    searq = models.CharField(max_length=100,blank = True,null=True,)
