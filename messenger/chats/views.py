from django.shortcuts import render
from chats.models import Chat
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_chat(request, is_group_chat, topic, last_message):
    if request.method == 'POST':
        if (is_group_chat == 0):
            is_group_chat = False
        elif (is_group_chat == 1):
            is_group_chat = True
        else:
            return JsonResponse({'error':'Invalid Syntax for is_group_chat'})
        Chat(is_group_chat = is_group_chat, topic = topic, last_message = last_message).save()
        return JsonResponse({'Result':'Well Done!'})
    return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def show_all(request):
    if request.method == 'GET':
        data = Chat.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])
    