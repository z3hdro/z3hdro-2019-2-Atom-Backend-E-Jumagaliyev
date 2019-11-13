from django.shortcuts import render
from chats.models import Chat
from chats.forms import ChatForm
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_chat(request):
    form = ChatForm(request.POST)
    if form.is_valid():
        chat = form.save()
        return JsonResponse({
            'Result':'Chat created',
            'id': chat.id
        })
    return JsonResponse({'error': form.errors}, status=400)


@csrf_exempt
def show_all_chats(request):
    if request.method == 'GET':
        data = Chat.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])
