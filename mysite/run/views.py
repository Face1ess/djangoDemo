from django.shortcuts import render_to_response
from run.models import T_Act
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.http import HttpResponse,HttpResponseRedirect
from run.forms import ContactForm,ActForm

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

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def contact_form(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            return HttpResponse(cd['message'])
    else:
        form = ContactForm()
    return render_to_response('contact_form.html',{'form':form})

def act_form(request):
    if request.method == 'POST' :
        form = ActForm(request.POST)
        if form.is_valid():
            return HttpResponse("Success")
        else :
            return HttpResponse("Failure")
    else :
        form = ActForm()
    return render_to_response('act_form.html',{'form':form})
         
