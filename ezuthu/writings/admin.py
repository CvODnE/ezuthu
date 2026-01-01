from django.contrib import admin
from .models import Writer, Writing

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')


@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer', 'writing_type', 'is_published')
    list_filter = ('writing_type', 'is_published')
    search_fields = ('title', 'content')