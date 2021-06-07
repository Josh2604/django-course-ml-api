from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Use cases
from users.core.usecases.user.user import UserCaseUser


# Create your views here.
@api_view(['GET'])
def get_all(request):
    users = UserCaseUser().get_users()
    return Response({"status": 200, "users": users}, status=200)


@api_view(['GET'])
def get_one(request, uid):
    user = UserCaseUser().get_user(uid)
    return Response({"status": 200, "user": user})


@api_view(['POST'])
def create_user(request):
    user = request.data
    return Response({"status": 200, "message": "OK, user created"})


@api_view(['PUT'])
def update_user(request, uid):
    return Response({"status": 200, "message": "OK, user updated"})


@api_view(['DELETE'])
def delete_user(request, uid):
    return Response({"status": 200, "message": "OK, user deleted"})
