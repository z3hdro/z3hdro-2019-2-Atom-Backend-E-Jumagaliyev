from chats.models import Chat
from django.conf import settings
from users.models import User
from message.models import Message
from members.models import Member
from attachment.models import Attachment
from message.forms import MessageForm
from django.http import JsonResponse, HttpResponse
from django.core.files.images import ImageFile
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage
import boto3

# Create your views here.


@api_view(['POST'])
def create_message(request):
    token = request.headers.get('Authorization')[6:]
    form = MessageForm(request.POST, request.FILES)
    if form.is_valid():
        # print(request.POST, request.FILES)
        data = request.POST
        my_id = Token.objects.filter(key=token).values('user_id')[0]['user_id']
        message = Message(chat_id=data['chat_id'], user_id=my_id, content=data['content'])
        session = boto3.Session()
        s3_client = session.client(service_name='s3',
                                   endpoint_url='http://hb.bizmrg.com',
                                   aws_access_key_id='ns3JMEzqS7GkxRcCuvRDVh',
                                   aws_secret_access_key='8DvkXKZkUdebaEkBfnyGKhJBZaMaW4ybJdxwiN2WzeEv')  
        if request.POST['attachment_type'] == 'null':
            print('without attachment')
            message.save()
            return JsonResponse({'Result':'Message created without attachment'})
        elif request.POST['attachment_type'] == 'images':
            print('with images')
            message.save()
            uploaded_file = request.FILES.getlist('media')
            for file in uploaded_file:
                print(file)
                url_location = 'attachments/chat' + data['chat_id'] + '/' + data['attachment_type'] + '/' + file.name + '-' + str(hash(file))
                s3_client.put_object(Bucket='z3hdro_messenger', Key=url_location, Body = file)
                attach = Attachment(chat_id=data['chat_id'], user_id=my_id, message_id=message.id, type_attachment=data['attachment_type'], url = url_location)
                attach.save()
            return JsonResponse({'Result':'Message created with image attachment'})
        elif request.POST['attachment_type'] == 'audio_message':
            print('with audio')
            message.save()
            uploaded_file = request.FILES['media']
            url_location = 'attachments/chat' + data['chat_id'] + '/' + data['attachment_type'] + '/' + 'audio-' + str(hash(uploaded_file))
            s3_client.put_object(Bucket='z3hdro_messenger', Key=url_location, Body = uploaded_file)
            attach = Attachment(chat_id=data['chat_id'], user_id=my_id, message_id=message.id, type_attachment=data['attachment_type'], url = url_location)
            attach.save()
            return JsonResponse({'Result':'Message created with audiorecord attachment'})
        elif request.POST['attachment_type'] == 'geolocation':
            print('with geolocation')
            message.save()
            attach = Attachment(chat_id=data['chat_id'], user_id=my_id, message_id=message.id, type_attachment=data['attachment_type'], url = data['geolocation_url'])
            attach.save()
            return JsonResponse({'Result':'Message created with geolocation'})
        return JsonResponse({'error':'unexpected bug'}, status=400)
    return JsonResponse({'error': form.errors}, status=400, json_dumps_params={'ensure_ascii': False})



@api_view(['GET'])
def show_all_messages(request):
    result = []
    token = request.headers.get('Authorization')[6:]
    data = Message.objects.filter(chat_id=request.GET['chat_id']).order_by('id').values()
    attachments = Attachment.objects.filter(chat_id=request.GET['chat_id']).values()
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url='http://hb.bizmrg.com',
                                aws_access_key_id='ns3JMEzqS7GkxRcCuvRDVh',
                                aws_secret_access_key='8DvkXKZkUdebaEkBfnyGKhJBZaMaW4ybJdxwiN2WzeEv')
    if len(data) == 0:
        return JsonResponse({'result':'chat is empty'})
    for message in data:
        related_attach = attachments.filter(message_id=message['id'])
        if len(related_attach) != 0:
            attach_url = []
            for url in related_attach:
                if url['type_attachment'] == 'geolocation':
                    local_url = url['url']
                else:
                    local_url = s3_client.generate_presigned_url('get_object',
                            Params={
                                'Bucket': 'z3hdro_messenger',
                                'Key': url['url'],
                            },
                            ExpiresIn=3600)
                attach_url.append(local_url)
            message['attachment_type'] = related_attach[0]['type_attachment'] 
            message['attachment_url'] = attach_url
        else:
            message['attachment_type'] = None
            message['attachment_url'] = None
        result.append(message)
    my_id = Token.objects.filter(key=token).values('user_id')[0]['user_id']
    you_author = User.objects.filter(id=my_id).values('username')[0]['username']
    other_id = Member.objects.filter(chat_id=request.GET['chat_id']).exclude(user_id = my_id).values('user_id')[0]['user_id']
    another_author = User.objects.filter(id=other_id).values('username')[0]['username']
    last_message_id = Message.objects.filter(chat_id=request.GET['chat_id']).filter(user_id=other_id).order_by('-id').values()
    if len(last_message_id) != 0:
        last_message_id = last_message_id[0]['id']
        Member.objects.filter(user_id=my_id).filter(chat_id=request.GET['chat_id']).update(last_read_message_id=last_message_id)
    return JsonResponse({'result': list(result), 'you': [you_author, my_id], 'other' :[another_author, other_id]})



@api_view(['GET'])
def show_all_group_messages(request):
    result = []
    token = request.headers.get('Authorization')[6:]
    data = Message.objects.filter(chat_id=request.GET['chat_id']).order_by('id').values()
    attachments = Attachment.objects.filter(chat_id=request.GET['chat_id']).values()
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url='http://hb.bizmrg.com',
                                aws_access_key_id='ns3JMEzqS7GkxRcCuvRDVh',
                                aws_secret_access_key='8DvkXKZkUdebaEkBfnyGKhJBZaMaW4ybJdxwiN2WzeEv')
    my_id = Token.objects.filter(key=token).values('user_id')[0]['user_id']
    you_author = User.objects.filter(id=my_id).values('username')[0]['username']
    other_id = Member.objects.filter(chat_id=request.GET['chat_id']).exclude(user_id = my_id).values('user_id')[0]['user_id']
    another_author = User.objects.filter(id=other_id).values('username')[0]['username']
    if len(data) == 0:
        return JsonResponse({'result':'chat is empty'})
    for message in data:
        related_attach = attachments.filter(message_id=message['id'])
        message_user_id = message['user_id']
        message['username'] = User.objects.filter(id=message_user_id).values('username')[0]['username']
        if len(related_attach) != 0:
            attach_url = []
            for url in related_attach:
                if url['type_attachment'] == 'geolocation':
                    local_url = url['url']
                else:
                    local_url = s3_client.generate_presigned_url('get_object',
                            Params={
                                'Bucket': 'z3hdro_messenger',
                                'Key': url['url'],
                            },
                            ExpiresIn=3600)
                attach_url.append(local_url)
            message['attachment_type'] = related_attach[0]['type_attachment'] 
            message['attachment_url'] = attach_url
        else:
            message['attachment_type'] = None
            message['attachment_url'] = None
        result.append(message)
    return JsonResponse({'result': list(result)})
