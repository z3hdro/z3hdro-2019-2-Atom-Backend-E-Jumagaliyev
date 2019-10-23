from django.shortcuts import render
from django.http import JsonResponse
import django.http

# Create your views here.

def user_profile(request):
    try:
        chats_id = request.GET.get('chats_id')
        user = chats_id.objects.get(id=chats_id)
    except user.DoesNotExit:
        raise http405
    return JsonResponse({'id':'228'})

def render_method(request, pk):
    print(pk)
    return render(request, 'chat_list.html')
    #return JsonResponse({'test':'KEK'})
