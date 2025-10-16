from django.shortcuts import render

# Create your views here.
from drf_spectacular.utils import extend_schema,OpenApiRequest
from rest_framework import generics, permissions
from .serializers import (
    StorageCreateSerializer,
    StorageEditSerializer,
    StorageInforamtionSerializer
)
from .models import Storage
from authenticate.models import User
from rest_framework.exceptions import PermissionDenied


class StorageCreateView(generics.CreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=OpenApiRequest(
            request={
                'type': 'object',
                'properties': {
                    'address': {
                        'type': 'string',
                        'example': 'Las Vegas, 12road st., build 20'},
                    'title': {
                        'type': 'string',
                        'example': 'Склад компании 123'
                    }

                }
            }
        ),
        responses={201: StorageCreateSerializer},
        tags=['Storage'],
        summary='Создание склада',
        description='Создает склад для компании'
    )

    def post(self, request, *args, **kwargs):
        return super().post(request,*args,**kwargs)


class StorageEditView(generics.UpdateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageEditSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=OpenApiRequest(
            request={
                'type': 'object',
                'properties': {
                    'address': {
                        'type': 'string',
                        'example': 'Las Vegas, 12road st., build 20'},
                    'title': {
                        'type': 'string',
                        'example': 'Склад компании 123'
                    }

                }
            }
        ),
        responses={201: StorageCreateSerializer},
        tags=['Storage'],
        summary='Изменение данных склада',
        description='Изменяет данные для склада компании'
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request,*args,**kwargs)


@extend_schema(tags=['Storage'],
               summary='Удаление склада из компании')
class StorageDeleteView(generics.DestroyAPIView):
    queryset = Storage.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        user = self.request.user

        if not user.is_company_owner or instance.company != user.company:
            raise PermissionDenied("Вы не можете удалить этот склад")

        instance.delete()

class StorageInforamtionView(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageInforamtionSerializer
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        request=OpenApiRequest(),
        responses=StorageInforamtionSerializer,
        tags=['Storage'],
        summary='Информация о складе',
        description='Получение данных о складе компании'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)