from django.contrib import admin

# Register your models here.
from .models import Diary


@admin.register(Diary)
class Diary(admin.ModelAdmin):
    pass
