from django.http import HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET"])
def appinfo(request):
    data = dict(name="pirple", about="pirple is a virtaul classroom manager.")
    return Response(data=data, status=status.HTTP_200_OK)