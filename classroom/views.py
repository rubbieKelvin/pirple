from django.shortcuts import render

# Create your views here.
from .serializers import UserSerializer
from .models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class UserRecordView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, format=None):
        users = User.objects.all()
        serializers = UserSerializer(users, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializers = UserSerializer(data=request.data)
        
        if serializers.is_valid(raise_exception=ValueError):
            serializers.create(validated_data=request.data)

            return Response(
                serializers.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            dict(
                error=True,
                error_msg=serializers.error_messages
            ),
            status=status.HTTP_400_BAD_REQUEST
        )