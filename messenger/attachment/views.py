from django.shortcuts import render
from attachment.models import Attachment
from attachment.forms import AttachmentForm
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_attachment(request):
    form = AttachmentForm(request.POST)
    if form.is_valid():
        attachemnt = form.save()
        return JsonResponse({
            'Result':'Attachemnt created',
            'id': attachemnt.id
        })
    return JsonResponse({'error': form.errors}, status=400)


@csrf_exempt
def show_all_attachments(request):
    if request.method == 'GET':
        data = Attachment.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])
