from rest_framework import serializers
from .models import Company
from authenticate.models import User


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['title', 'inn']

    def validate_inn(self, value):
        if len(value) > 12:
            raise serializers.ValidationError('Инн не должен быть больше 12 символов')
        return value

    def create(self, validated_data):
        user = self.context['request'].user

        if user.is_company_owner:
            raise serializers.ValidationError("Вы уже являетесь владельцем компании")

        if user.company_id:
            raise serializers.ValidationError("Вы уже состоите в компании")

        company = Company.objects.create(owner=user, **validated_data)

        user.company = company
        user.is_company_owner = True
        user.save()

        return company


class CompanyAddEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate_email(self, value):
        try:
            search_user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким email не найден")

        if search_user.company is not None:
            raise serializers.ValidationError("Пользователь уже состоит в компании")

        self.users_to_add = search_user

        return value

    def update(self, instance, validated_data):
        current_user = self.context['request'].user

        if not current_user.is_company_owner:
            raise serializers.ValidationError("Добавлять сотрудников может только владелец компании")

        instance.company = current_user.company
        instance.save()

        return instance


class CompanyRemoveEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

    def validate_email(self, value):
        try:
            search_user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким email не найден")

        current_user = self.context['request'].user
        if search_user.company != getattr(current_user, 'company', None):
            raise serializers.ValidationError('Пользователь не состоит в вашей компании')

        return value

    def update(self, instance, validated_data):

        current_user = self.context['request'].user

        if not current_user.is_company_owner:
            raise serializers.ValidationError("Вы не можете увольнять сотрудников")

        instance.company = None
        instance.save()
        return instance



class CompanyInforamtionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

