from django.shortcuts import render
from django.http import HttpResponse 
from django.template.loader import get_template
from django.template import Context
from run.models import T_Act
from django.core.paginator import Paginator

# Create your views here.
def runInfo(request):
    itemData = T_Act.objects.all().order_by('-id')
    itemList = Paginator(itemData,10)
    pNum = 1
    itemListByPage = itemList.page(pNum).object_list 
    t = get_template('runMainTemplate.html')
    html = t.render(Context({'itemListByPage':itemListByPage})) 
    return HttpResponse(html)
