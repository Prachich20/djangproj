from django.db import models
from django.contrib.auth.models import User

class Invitation(models.Model):
    from_user = models.ForeignKey(User, related_name="invitations_sent",on_delete= models.DO_NOTHING)
    to_user =models.ForeignKey(User, related_name= "invitations_received", on_delete=models.DO_NOTHING)
    message = models.CharField(max_length= 300)
    timestamp = models.DateField(auto_now_add= True)
