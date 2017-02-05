from rest_framework import serializers

from conversation.models import Conversation

class ConversationSerializer(serializers.Serializer):
    '''
    User conversation serializer
    '''
    class Meta:
        model = Conversation
        depth = 1