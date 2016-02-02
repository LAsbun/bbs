from django.shortcuts import render_to_response, HttpResponse
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from app01.models import News
import json

# Create your views here.
def index(request):
    news_list = News.objects.all()
    context = {
        'news_list':news_list,
    }
    return render_to_response('index.html', context, context_instance=RequestContext(request))

@csrf_exempt
def addfavor(request):

    ret = {'status':0, 'data':'', 'message':'',}

    try:
        id = request.POST.get('nid', None)
        obj = News.objects.get(id=id)
        temp = obj.favor_count + 1
        obj.favor_count = temp
        obj.save()
        ret['data'] = temp
        ret['status'] = 1

    except Exception, e:
        ret['message'] = e.message

    return HttpResponse(json.dumps(ret))