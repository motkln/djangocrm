from django.urls import path
from .views import (
    StorageCreateView,
    StorageEditView,
    StorageDeleteView,
    StorageInforamtionView
)

urlpatterns = [
    path(
      'register/', StorageCreateView.as_view(),name='Создать склад'
    ),
    path(
      'edit/<int:pk>',  StorageEditView.as_view(),name='Изменить данные склада'
    ),
    path(
        'delete/<int:pk>', StorageDeleteView.as_view(),name='Удалить склад из компании'
    ),
    path(
        'about_storage', StorageInforamtionView.as_view(),name='Получить информацию о складе компании'
    )
]