from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    from_user = models.ForeignKey(User, related_name = 'fromuser')
    to_user = models.ForeignKey(User, related_name = 'touser')
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
