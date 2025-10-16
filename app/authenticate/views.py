from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from drf_spectacular.utils import extend_schema,OpenApiRequest
from .serializers import RegisterSerializer,CustomTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = []
    @extend_schema(
        request=OpenApiRequest(
            request={
                'type':'object',
                'properties':{
                    'email': {
                        'type':'string',
                        'example':'example@gmail.com'},
                    'password':{
                        'type':'string',
                        'example':'12345678'
                    }

                }
            }
        ),
        responses={201: RegisterSerializer},
        tags=['Registration'],
        summary='Регистрация нового пользователя',
    )
    def post(self, request):
       serializer = RegisterSerializer(data=request.data)
       if serializer.is_valid():
           user = serializer.save()
           return Response(serializer.data,status=status.HTTP_201_CREATED)
       else:
           return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


class CustomObtainTokenView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


