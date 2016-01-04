from django.shortcuts import render_to_response
from run.models import T_Act
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage

# Create your views here.
def runInfo(request):
    itemData = T_Act.objects.all().order_by('-id')
    paginator = Paginator(itemData,8)
    page = request.GET.get('page')
    try:
        itemList = paginator.page(page)
    except PageNotAnInteger :
        itemList = paginator.page(1)
    except EmptyPage:
        itemList = paginator.page(paginator.num_pages)
    return render_to_response('runMainTemplate.html',{"itemList":itemList})
