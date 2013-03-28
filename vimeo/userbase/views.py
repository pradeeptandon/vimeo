import csv
from userbase.models import user_data 
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from userbase.forms import sq

def data_entry():
    inp = open('result1.csv', 'rb')
    reader = csv.reader(inp, delimiter=',')
    j = 0
    print reader
    for row in reader:
        database = user_data(username = str(row[0]), url = str(row[1]), payment = str(row[2]),videos =str(row[3]) ,staff_pick=str(row[4]))
        database.save()
        
        print j
        j = j+1

    inp.close()

def display(request):
    result = user_data.objects.all()
    form = sq()
    context ={'result': result,'form':form,}
    return render_to_response('display.html',context,context_instance= RequestContext(request))


def filt(request):
    if request.method == 'POST':
        form = sq(request.POST)
        if form.is_valid():
	    queries = form.cleaned_data['searq']
	    if len(queries) ==0:
	        result = user_data.objects.all()
	        context = {'result':result,}
	        return render_to_response('display.html',context,context_instance = RequestContext(request))
	    else:
                length = len(queries)
	        result = user_data.objects.filter(username__icontains=str(queries))
	        context = {'result':result,'form':form,'query':queries,}
	        return render_to_response('display.html',context,context_instance=RequestContext(request))
	else:
	    result = user_data.objects.all()
            form = sq()
            context = {'result':result,'form':form,}
	    return render_to_response('error.html',context,context_instance=RequestContext(request))
    else:
	result = user_data.objects.all()
	form = sq()
	context = {'result':result,'form':form,}
	return render_to_response('display.html',context,context_instance=RequestContext(request))

def filt_pay(request,queries):
    result = user_data.objects.filter(username__icontains=str(queries),payment__icontains = 'YES')
    form = sq()
    context = {'result':result,'form':form,'query':queries,}
    return render_to_response('display.html',context,context_instance=RequestContext(request))
    
def filt_vid(request,queries):
    result = user_data.objects.filter(username__icontains=str(queries),videos__icontains = 'YES')
    form = sq()
    context = {'result':result,'form':form,'query':queries,}
    return render_to_response('display.html',context,context_instance=RequestContext(request))
def filt_sp(request,queries):    
    result = user_data.objects.filter(username__icontains=str(queries),staff_pick__icontains = 'YES')
    form = sq()
    context = {'result':result,'form':form,'query':queries,}
    return render_to_response('display.html',context,context_instance=RequestContext(request))


