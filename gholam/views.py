from django.shortcuts import render_to_response
from ups.models import UserPass
from logic import Gholam
from django.http import HttpResponse

def index(request):
    return render_to_response("index.html")

def loginCheck(request):
    username = request.GET['username']
    password = request.GET['password']
    for i in UserPass.objects.all():
        if i.username == username and i.password == password:
            return render_to_response("gholam.html")
    return render_to_response("index.html", {"error": "True"})

def logic(request):
    user = request.GET['username']
    chan = request.GET['channel']
    if user and chan:
        Gholam(user, chan).listen()
        return HttpResponse("logining ...")
    else:
        return render_to_response("gholam.html", {"error": "True"})