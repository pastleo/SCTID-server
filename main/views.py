import json

from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
# See https://docs.djangoproject.com/en/1.8/topics/auth/default/#django.contrib.auth.decorators.login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.http.response import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .models import *



def index(request):
    return render(request, 'main/index.html', {})

@csrf_exempt
def logout(request):
    auth_logout(request)
    return HttpResponse(json.dumps({"success":True, "message":"Logout success"}), content_type="application/json")

@csrf_exempt
def login(request):
    response_data = {}
    response_data['success'] = False
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                response_data['message'] = "Login success"
                response_data['success'] = True
            else:
                raise Exception("Account disabled")
        else:
            raise Exception("Invalid login")
    except KeyError as e:
        response_data['message'] = "Please input username and password"
    except Exception as e:
        response_data['message'] = "%s" % e

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required(login_url='/notLogin')
@csrf_exempt
def register(request):
    response_data = {}
    response_data['success'] = False
    try:
        si,is_new = Sctid.objects.get_or_create(card_id=request.POST['card_id'])
        si.student_id = request.POST['student_id']
        si.save()
        response_data['success'] = True
        response_data['message'] = "OK"
        if not is_new:
            response_data['message'] = "OK, overwritten"
    except KeyError as e:
        response_data['message'] = "Please input card_id and student_id %s" % e
    except Exception as e:
        response_data["message"] = "%s" % e

    return HttpResponse(json.dumps(response_data), content_type="application/json")

@login_required(login_url='/notLogin')
@csrf_exempt
def get(request):
    response_data = {}
    response_data['success'] = False
    try:
        si = get_object_or_404(Sctid,card_id=request.POST['card_id'])
        response_data["student_id"] = si.student_id
        response_data['success'] = True
        response_data['message'] = "OK, Student ID is %s" % si.student_id
    except KeyError as e:
        response_data['message'] = "Please input card_id"
    except Http404 as e:
        response_data['message'] = "Card ID not found"
    except Exception as e:
        response_data["message"] = "%s" % e

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def notLogin(request):
    return HttpResponse(json.dumps({"success":False, "message":"You haven login"}), content_type="application/json")

