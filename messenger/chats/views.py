from chats.models import Chat
from users.models import User
from message.models import Message
from members.models import Member
from chats.forms import ChatForm
from django.http import JsonResponse, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
import boto3


# Create your views here.
@api_view(['POST'])
def create_chat(request):
    print(request.POST)
    token = request.headers.get('Authorization')[6:]
    form = ChatForm(request.POST)
    if form.is_valid():
        if request.POST['is_group_chat'] == 'false':
            print('passed false')
            group_chat_status = False
            UserInput = User.objects.filter(username=request.POST['username']).values('id')
            if len(UserInput) is 0:
                return HttpResponse('Bad Request', status=400)
            firstMember_me = Token.objects.filter(key=token).values('user_id')[0]['user_id']
            secondMember = UserInput[0]['id']
            arr = []
            for element in Member.objects.filter(user_id=firstMember_me).values('chat_id'):
                arr.append(element['chat_id'])
            for element in Member.objects.filter(user_id=secondMember).values('chat_id'):
                if element['chat_id'] in  arr:
                    print('Already exists')
                    return JsonResponse({'error': 'Already exists'}, status=400)
            chat = Chat(is_group_chat = group_chat_status, topic = request.POST['topic'], last_message = '')
            chat.save()
            Member.objects.create(user_id=firstMember_me, chat_id = chat.id)
            Member.objects.create(user_id=secondMember, chat_id = chat.id)
            return JsonResponse({
                'Result':'Chat created',
                'id': chat.id,
                'topic': chat.topic
            }, json_dumps_params={'ensure_ascii': False})
        elif request.POST['is_group_chat'] == 'true':
            print('passed true')
            print(request.POST.getlist('username'))
            print(request.POST['topic'])
            group_chat_status = True
            my_id = Token.objects.filter(key=token).values('user_id')[0]['user_id']
            userlist = request.POST.getlist('username')
            chat = Chat(is_group_chat=group_chat_status, topic=request.POST['topic'], last_message='')
            chat.save()
            Member.objects.create(user_id=my_id, chat_id=chat.id)
            if len(userlist) == 0:
                return JsonResponse({'result': 'users not seleceted'})
            else:
                for user in userlist:
                    user_id = User.objects.filter(username = user).values('id')[0]['id']
                    Member.objects.create(user_id=user_id, chat_id=chat.id)
            return JsonResponse({
                'Result':'Group chat created',
                'id': chat.id,
                'topic': chat.topic
            }, json_dumps_params={'ensure_ascii': False})
        else:
            print('nothing passed')
            return JsonResponse({'error': 'is_group_chat is bad'}, status=400)
    return JsonResponse({'error': form.errors}, status=400, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def show_all_chats(request):
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url='http://hb.bizmrg.com',
                                aws_access_key_id='ns3JMEzqS7GkxRcCuvRDVh',
                                aws_secret_access_key='8DvkXKZkUdebaEkBfnyGKhJBZaMaW4ybJdxwiN2WzeEv')
    token = request.headers.get('Authorization')[6:]
    data_to_send = []
    user_data = Token.objects.filter(key=token).values('user_id')[0]['user_id']
    data = Member.objects.filter(user_id = user_data).values('chat_id','last_read_message_id')
    if len(data) == 0:
        return JsonResponse({'names':'NO CHATS'})
    for index in range(len(data)):
        chat_index = data[index]['chat_id']
        chat_data = Chat.objects.filter(id = chat_index).values('id','is_group_chat','topic','last_message')[0]
        if chat_data['is_group_chat'] == 'false':
            person_id = Member.objects.filter(chat_id=chat_index).exclude(user_id=user_data).values('user_id')[0]['user_id']
            avatar_url = s3_client.generate_presigned_url('get_object',
                                    Params={
                                        'Bucket': 'z3hdro_messenger',
                                        'Key': User.objects.filter(id=person_id).values('avatar')[0]['avatar'],
                                    },
                                    ExpiresIn=3600)
            chat_data['avatar'] = avatar_url
        else:
            avatar_url = s3_client.generate_presigned_url('get_object',
                                    Params={
                                        'Bucket': 'z3hdro_messenger',
                                        'Key': 'avatar/AvatarNone.png',
                                    },
                                    ExpiresIn=3600)
            chat_data['avatar'] = avatar_url
        last_message_id = data[index]['last_read_message_id']
        if last_message_id != None:
            chat_data['last_message'] = Message.objects.filter(id=last_message_id).values('content')[0]['content']
            chat_data['last_message_time'] = Message.objects.filter(id=last_message_id).values('added_at')[0]['added_at']
        else:
            chat_data['last_message'] = ''
            chat_data['last_message_time'] = ''
        data_to_send.append(chat_data)
    return JsonResponse({'names': data_to_send})

@api_view(['GET'])
def show_special_chat(request):
    if len(request.GET) == 0:
        return JsonResponse({'Error', 'Get parameter is wrong'}, status=400)
    data = Chat.objects.filter(id=request.GET['chat_id']).values()
    return JsonResponse({'result': data[0]['topic']})