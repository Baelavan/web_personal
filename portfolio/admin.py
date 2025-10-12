from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured']
    list_filter = ['category', 'featured']
    search_fields = ['title', 'description']