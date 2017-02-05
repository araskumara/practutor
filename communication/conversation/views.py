from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from conversation.models import Conversation
from conversation.serializer import ConversationSerializer

    
@api_view('GET')
def get_recent_conversation(request):
    '''
    This api gets the recent conversation of all the users with the message text
    '''
    # distinct 'from user' from conversation model
    conversations = Conversation.objects.values('from_user').distinct()
    if conversations:
        # append each user to a list
        distinct_users_list = []
        for conversation in conversations:
            distinct_users_list.append(conversation['from_user'])
            # for each user in the list retrieve the lastest conversation id(primary key)
        recent_conversation_id_list = []
        for user in distinct_users_list:
            conversation = Conversation.objects.filter(from_user = user).values('id'). \
                                                    order_by('-created_date')[0]
            # add each id to another list
            recent_conversation_id_list = conversation['id']
        # for the list of ids, retrieve the objects 
        recent_conversations = Conversation.objects.filter(id__in = recent_conversation_id_list)
        # serialize the queryset
        recent_conversations_serializer = ConversationSerializer(recent_conversations, many = True)
        return Response(recent_conversations_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('no conversations', status=status.HTTP_200_OK)

    
@api_view('POST')
def send_message_other_user(request):
    '''
    This api saves the conversation posted by one user to another user
    '''
    to_user = User.objects.get(username = request.POST['to_username'])
    Conversation.objects.create(
        from_user = request.user, to_user = to_user, message = request.POST['message']
    )
    return Response('message posted successfully', status=status.HTTP_200_OK)
    
    
@api_view('POST')
def get_conversation_between_user(request):
    '''
    This api gets all the conversation between two given users..
    let us say the parameters are user_a and user_b
    '''
    between_conversations = Conversation.objects.filter(
        from_user = User.objects.get(username = request.POST['user_a']),
        to_user = User.objects.get(username = request.POST['user_b'])
    )
    if between_conversations:
        #serialize the queryset
        between_conversations_serializer = ConversationSerializer(between_conversations, many = True)
        return Response(between_conversations_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response('no conversations', status=status.HTTP_200_OK)
