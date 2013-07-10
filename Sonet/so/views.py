# Create your views here.
#coding=utf-8
from django.http import *
from django.shortcuts import *
import datetime


def hello(request):
    return HttpResponse("hello word")

def loginAction(request):
    """

    :param request:
    :return:
    """
    time = datetime.datetime.now()

    return render_to_response('login.html',{'time':time})
