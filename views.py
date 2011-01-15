from django.shortcuts import render_to_response
from logic import Gholam
from django.http import HttpResponse

def index(request):
    return render_to_response("index.html")

def logic(request):
    user = request.GET['username']
    chan = request.GET['channel']
    if user and chan:
        Gholam(user, chan).listen()
        return HttpResponse("logining ...")
    else:
        return render_to_response("index.html", {"error": "True"})