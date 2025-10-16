from rest_framework import serializers
from .models import Storage


class StorageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['address', 'title']

    def create(self, validated_data):
        user = self.context['request'].user
        company = user.company

        if Storage.objects.filter(company=company).exists():
            raise serializers.ValidationError("У этой компании уже есть склад")

        if not user.is_company_owner:
            raise serializers.ValidationError("У вас не права создавать склад в компанию")

        storage = Storage.objects.create(company=company, **validated_data)
        storage.save()

        return storage


class StorageEditSerializer(StorageCreateSerializer):
    class Meta:
        model = Storage
        fields = ['address','title']

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if not user.is_company_owner:
            raise serializers.ValidationError("У вас не права изменять данные склада")

        instance.title = validated_data.get('title',instance.title)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance

class StorageInforamtionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'



