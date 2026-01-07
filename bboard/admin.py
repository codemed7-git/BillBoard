from django.contrib import admin
from .models import Bb, Rubric

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'rubric', 'price', 'author', 'published', 'is_active')
    list_display_links = ('title',)
    list_filter = ('rubric', 'published', 'is_active')
    search_fields = ('title', 'content')
    list_editable = ('is_active',)
    date_hierarchy = 'published'
    fields = (('title', 'rubric'), 'content', 'price', 'author', 'is_active')

admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, RubricAdmin)