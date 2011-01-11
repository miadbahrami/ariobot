from django.db import models

class UserPass(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.username + " " + self.password
