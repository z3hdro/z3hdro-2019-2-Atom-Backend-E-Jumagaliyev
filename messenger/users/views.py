from users.models import User
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from users.forms import UserForm
import boto3

@api_view(['GET'])
def show_all_users(request):
    token = request.headers.get('Authorization')[6:]
    authorized_user = Token.objects.filter(key = token)
    data_to_send = []    
    data = User.objects.all().order_by('id').values('id','username')
    for i in range(len(data)):
        if data[i]['id'] is not authorized_user.values('user_id')[0]['user_id']:
            data_to_send.append(data[i])
    return JsonResponse({'result': data_to_send })


@api_view(['POST'])
def update_data_on_user(request):
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url='http://hb.bizmrg.com',
                                aws_access_key_id='ns3JMEzqS7GkxRcCuvRDVh',
                                aws_secret_access_key='8DvkXKZkUdebaEkBfnyGKhJBZaMaW4ybJdxwiN2WzeEv')
    form = UserForm(request.POST, request.FILES)
    token = request.headers.get('Authorization')[6:]
    authorized_user_id = Token.objects.filter(key = token).values('user_id')[0]['user_id']
    data = request.POST
    if form.is_valid():
        print(type(authorized_user_id))
        print(request.FILES['avatar'])
        url_location = 'avatar/' + str(authorized_user_id) + str(request.FILES['avatar'])
        s3_client.put_object(Bucket='z3hdro_messenger', Key=url_location, Body = request.FILES['avatar'])
        me = User.objects.filter(id = authorized_user_id).update(first_name=data['first_name'],last_name=data['last_name'],bio=data['bio'],avatar=url_location)
        print('data is changed')
        return JsonResponse({'success': 'userinfo is updated'})
    return JsonResponse({'error': 'user is not updated' }, status=400)


@api_view(['GET'])
def find_user(request):
    session = boto3.Session()
    s3_client = session.client(service_name='s3',
                                endpoint_url='http://hb.bizmrg.com',
                                aws_access_key_id='ns3JMEzqS7GkxRcCuvRDVh',
                                aws_secret_access_key='8DvkXKZkUdebaEkBfnyGKhJBZaMaW4ybJdxwiN2WzeEv')
    token = request.headers.get('Authorization')[6:]
    authorized_user_id = Token.objects.filter(key = token).values('user_id')[0]['user_id']
    me = User.objects.filter(id = authorized_user_id).values('first_name','last_name','bio','avatar')[0]
    avatar_url = s3_client.generate_presigned_url('get_object',
                                Params={
                                    'Bucket': 'z3hdro_messenger',
                                    'Key': me['avatar'],
                                },
                                ExpiresIn=3600)
    me['avatar'] = avatar_url
    return JsonResponse({'result': me})

@api_view(['GET'])
def find_my_id(request):
    token = request.headers.get('Authorization')[6:]
    my_id = Token.objects.filter(key = token).values('user_id')[0]['user_id']
    return JsonResponse({'result': my_id})