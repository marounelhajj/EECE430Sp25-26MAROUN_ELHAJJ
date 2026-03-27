from django.contrib import admin
from .models import VolleyPlayer

@admin.register(VolleyPlayer)
class VolleyPlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'position', 'date_joined', 'salary', 'contact_person']
    search_fields = ['name', 'position', 'contact_person']
    list_filter = ['position']
