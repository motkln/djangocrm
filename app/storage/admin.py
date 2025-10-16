from django.contrib import admin
from storage.models import Storage
# Register your models here.
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id','company','title','address')
    list_display_links = ('company',)