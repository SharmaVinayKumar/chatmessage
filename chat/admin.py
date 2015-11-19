from django.contrib import admin
from chat.models import Message, MessageUserList


class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'body','created_time' )


class MessageUserListAdmin(admin.ModelAdmin):
    list_display = ('requested_user', 'to_user', 'message')

admin.site.register(Message, MessageAdmin)
admin.site.register(MessageUserList, MessageUserListAdmin)