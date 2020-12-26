from django.contrib import admin
from .models import Degree, Field

@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    pass

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',),}
    pass