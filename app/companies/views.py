from django.shortcuts import render
from drf_spectacular.utils import extend_schema,OpenApiRequest
from rest_framework import generics, permissions
from .serializers import CompanyCreateSerializer, CompanyAddEmployeeSerializer, CompanyRemoveEmployeeSerializer, \
    CompanyInforamtionSerializer
from .models import Company
from authenticate.models import User

class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=OpenApiRequest(
            request={
                'type': 'object',
                'properties': {
                    'inn': {
                        'type': 'string',
                        'example': '123456789123'},
                    'title': {
                        'type': 'string',
                        'example': 'Рога и копыта'
                    }

                }
            }
        ),
        responses={201: CompanyCreateSerializer},
        tags=['Company'],
        summary='Создание компании',
        description='Создает компанию пользователю и делает его владельцем'
    )

    def post(self, request, *args, **kwargs):
        return super().post(request,*args,**kwargs)


class CompanyAddEmployeeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CompanyAddEmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        email = self.request.data.get('email')
        return User.objects.get(email=email)

    @extend_schema(
        request=OpenApiRequest(
            request={
                'type':'object',
                'properties': {
                    'email':{
                        'type':'string',
                        'example': 'gmail@gmail.com'
                    }
                },
                'required': ['email']
            }
        ),
        responses=CompanyCreateSerializer,
        tags=['Company'],
        summary='Добавление сотрудника',
        description='Добавление сотрудника в компанию владельцем компании'
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request,*args,**kwargs)


class CompanyRemoveEmployeeView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = CompanyRemoveEmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        email = self.request.data.get('email')
        return User.objects.get(email=email)

    @extend_schema(
        request=OpenApiRequest(
            request={
                'type':'object',
                'properties': {
                    'email':{
                        'type':'string',
                        'example': 'gmail@gmail.com'
                    }
                },
                'required': ['email']
            }
        ),
        responses=CompanyRemoveEmployeeSerializer,
        tags=['Company'],
        summary='Увольнение сотрудника',
        description='Удаление сотрудника из компании, доступно только владельцу'
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request,*args,**kwargs)


class CompanyInformationView(generics.ListAPIView):
    serializer_class = CompanyInforamtionSerializer
    permission_classes = [permissions.IsAuthenticated]
    @extend_schema(
        request=OpenApiRequest(
            request={
                'type': 'object',
                'properties': {
                    'inn': {
                        'type': 'string',
                        'example': '123456789012'
                    }
                },
                'required': ['inn']
            }
        ),
        responses=CompanyInforamtionSerializer,
        tags=['Company'],
        summary='Информация о компании',
        description='Получение данных о компании'
    )
    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)


