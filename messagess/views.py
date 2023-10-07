from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Message
from .serializers import MessageSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['message_id', 'sender_number', 'receiver_number']

    def get_queryset(self):
        account_id = self.kwargs.get('account_id', None)
        if account_id:
            return Message.objects.filter(account_id=account_id)
        return super().get_queryset()

@api_view(['POST'])
def create_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

def get_messages(request, account_id):
    # Retrieve messages for the provided account_id
    messages = Message.objects.filter(account_id=account_id)
    
    # Serialize the messages to JSON
    message_data = [{'message_id': message.message_id, 'sender_number': message.sender_number, 'receiver_number': message.receiver_number} for message in messages]
    
    return JsonResponse({'messages': message_data})

# def search_messages(request):
#     # Get query parameters from the request
#     message_id = request.GET.get('message_id', '')
#     sender_number = request.GET.get('sender_number', '')
#     receiver_number = request.GET.get('receiver_number', '')

#     # Build a query using Q objects
#     query = Q()
#     if message_id:
#         query |= Q(message_id=message_id)
#     if sender_number:
#         query |= Q(sender_number=sender_number)
#     if receiver_number:
#         query |= Q(receiver_number=receiver_number)

#     # Execute the query and retrieve matching messages
#     messages = Message.objects.filter(query)

#     # Serialize the messages to JSON
#     message_data = [{'message_id': message.message_id, 'sender_number': message.sender_number, 'receiver_number': message.receiver_number} for message in messages]

#     return JsonResponse({'messages': message_data})

def search_messages(request):
    message_ids = request.GET.get('message_id', '').split(',')
    sender_numbers = request.GET.get('sender_number', '').split(',')
    receiver_numbers = request.GET.get('receiver_number', '').split(',')

    query = Q()

    if message_ids and message_ids[0]:  # check if list is not empty
        query &= Q(message_id__in=message_ids)
    
    if sender_numbers and sender_numbers[0]:  # check if list is not empty
        query &= Q(sender_number__in=sender_numbers)
    
    if receiver_numbers and receiver_numbers[0]:  # check if list is not empty
        query &= Q(receiver_number__in=receiver_numbers)

    messages = Message.objects.filter(query)

    message_data = [
        {
            'message_id': message.message_id,
            'sender_number': message.sender_number,
            'receiver_number': message.receiver_number
        } 
        for message in messages
    ]

    return JsonResponse({'messages': message_data})


def lol(request):
    return "lol"