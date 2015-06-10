from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
import json


# Create your views here.
def displayEditor(request):
    
    html = request.session.get('html', '')
    css  = request.session.get('css', '')
    
    return render_to_response('editor/home.phtml', {'html': html,'css': css},
                          context_instance=RequestContext(request))

@csrf_exempt
def saveData(request):
    json_data   = json.loads(request.body)
    html    = json_data.get('html', '')
    css     = json_data.get('css', '')
    
    request.session['html'] = html
    request.session['css'] = css
    
    return HttpResponse()

@csrf_exempt
def render(request):
        
    html = request.session.get('html', '')
    css  = request.session.get('css', '')
    

    return render_to_response('editor/render.phtml', {'html': html,'css': css},
                      context_instance=RequestContext(request))