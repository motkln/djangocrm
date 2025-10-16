from django.urls import path
from .views import (
    CompanyCreateView,
    CompanyAddEmployeeView,
    CompanyRemoveEmployeeView,
    CompanyInformationView
)

urlpatterns = [
    path(
        'create/', CompanyCreateView.as_view(), name='Создать компанию'
    ),
    path(
        'add_user/',CompanyAddEmployeeView.as_view(),name='Добавить сотрудника'
    ),
    path(
        'delete_user/',CompanyRemoveEmployeeView.as_view(),name='Удаление сотрудника'
    ),
    path(
        'about_company',CompanyInformationView.as_view(),name='Информация о компании'
    )
]
