from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
import json


# this view simply tries to grab any html or css values from the session
# whether they exist or not we'll pass them on as variables to the template
def displayEditor(request):
    
    html = request.session.get('html', '')
    css  = request.session.get('css', '')
    
    return render_to_response('editor/home.phtml', {'html': html,'css': css},
                          context_instance=RequestContext(request))

# Here is where we extract our JSON data and store
# it in the session
@csrf_exempt
def saveData(request):
    json_data   = json.loads(request.body)
    html        = json_data.get('html', '')
    css         = json_data.get('css', '')
    
    request.session['html'] = html
    request.session['css'] = css
    
    return HttpResponse()

# this method takes our session variables and put them
# into variables and passed on into a template
@csrf_exempt
def render(request):
        
    html = request.session.get('html', '')
    css  = request.session.get('css', '')
    
    return render_to_response('editor/render.phtml', {'html': html,'css': css},
                      context_instance=RequestContext(request))