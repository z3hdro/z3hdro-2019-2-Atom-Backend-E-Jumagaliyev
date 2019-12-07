from attachment.models import Attachment
from message.models import Message
from attachment.forms import AttachmentForm
from django.http import JsonResponse, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def create_attachment(request):
    print(request.POST)
    form = AttachmentForm(request.POST)
    if form.is_valid():
        print(request.POST)
        return JsonResponse({'Result':'Attachemnt created'})
    return JsonResponse({'error': form.errors}, status=400)


# @csrf_exempt
# def show_all_attachments(request):
#     if request.method == 'GET':
#         data = Attachment.objects.all().order_by('id').values()
#         return JsonResponse({'result': list(data)})
#     return HttpResponseNotAllowed(['GET'])
