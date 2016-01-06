from django.shortcuts import render_to_response
from run.models import T_Act
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.http import HttpResponse,HttpResponseRedirect
from run.forms import ActForm

# Create your views here.
def runInfo(request):
    if request.method == 'POST' :
        form = ActForm(request.POST)
        if form.is_valid():
             cd = form.cleaned_data
             act = T_Act(T_ActDist=cd['actDist'], T_ActType=cd['actType'], T_ActDuration=cd['actDuration'], T_ActStartDate=cd['actStartDate'], T_ActAvgSpd=cd['actAvgSpd'], T_ActCalBurn=cd['actCalBurn'])
             act.save()
             return HttpResponseRedirect('/run/')
        else:
             return render_to_response('runAddError.html',{'form':form})
    else:
        itemData = T_Act.objects.all().order_by('-id')
        paginator = Paginator(itemData,8)
        page = request.GET.get('page')
        form = ActForm()
        try:
            itemList = paginator.page(page)
        except PageNotAnInteger :
            itemList = paginator.page(1)
        except EmptyPage:
            itemList = paginator.page(paginator.num_pages)
        return render_to_response('runMainTemplate.html',{"itemList":itemList,'form':form})
         
