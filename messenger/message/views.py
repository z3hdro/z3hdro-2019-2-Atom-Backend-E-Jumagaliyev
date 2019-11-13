from django.shortcuts import render
from message.models import Message
from message.forms import MessageForm
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_message(request):
    form = MessageForm(request.POST)
    if form.is_valid():
        message = form.save()
        return JsonResponse({
            'Result':'Message created',
            'id': message.id
        })
    return JsonResponse({'error': form.errors}, status=400)


@csrf_exempt
def show_all_messages(request):
    if request.method == 'GET':
        data = Message.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])
