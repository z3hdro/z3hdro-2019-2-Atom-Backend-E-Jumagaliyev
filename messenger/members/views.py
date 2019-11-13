from django.shortcuts import render
from members.models import Member
from members.forms import MemberForm
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def create_member(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        member = form.save()
        return JsonResponse({
            'Result':'Member created',
            'id': member.id
        })
    return JsonResponse({'error': form.errors}, status=400)


@csrf_exempt
def show_all_members(request):
    if request.method == 'GET':
        data = Member.objects.all().order_by('id').values()
        return JsonResponse({'result': list(data)})
    return HttpResponseNotAllowed(['GET'])
