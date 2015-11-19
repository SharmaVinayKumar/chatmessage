from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    """
    This Message model will save all communication between two user.
    """
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now=True)


class MessageUserList(models.Model):
    """
    This model will install user list
    """
    requested_user = models.ForeignKey(User, related_name='requested_user')
    to_user = models.ForeignKey(User, related_name='to_user_list')
    message = models.ForeignKey(Message)
    created_time = models.DateTimeField(auto_now=True)