'''
conversation app: url definitions
'''
from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^get_recent_conversation/$', views.get_recent_conversation),
    url(r'^send_message_other_user/$', views.send_message_other_user),
    url(r'^get_conversation_between_user/$', views.get_conversation_between_user),
]