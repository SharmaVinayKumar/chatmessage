from django.db import models
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


class Message(models.Model):
    """
    This Message model will save all communication between two user.
    """
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.body


class MessageUserList(models.Model):
    """
    This model will install user list
    """
    requested_user = models.ForeignKey(User, related_name='requested_user')
    to_user = models.ForeignKey(User, related_name='to_user_list')
    message = models.ForeignKey(Message, null=True, blank=True)
    created_time = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('requested_user', 'to_user',)


@receiver(post_save, sender=Message, dispatch_uid="save_user_list")
def saveuserlist(sender, instance,  **kwargs):
    """
    this is use for to save data for unique user list
    """
    try:
        obj, status = MessageUserList.objects.get_or_create(
                                    requested_user=instance.from_user,\
                                    to_user=instance.to_user)
        obj.message = instance
        obj.save()
        obj, status = MessageUserList.objects.get_or_create(
                                    requested_user=instance.to_user,\
                                    to_user=instance.from_user)
        obj.message = instance
        obj.save()
    except:
        pass
    
        