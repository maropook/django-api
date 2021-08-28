from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class Rodo(admin.ModelAdmin):
    pass
