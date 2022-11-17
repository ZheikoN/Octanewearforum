from django.contrib import admin
from .models import Post, Thread, Section
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Thread)
class ThreadAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    list_display = ('title', 'slug', 'status', 'created_on')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('body')
    list_filter = ('thread', 'created_on')
    list_display = ('thread', 'name', 'body')
    actions = ['disable_comments']
    
    def disable_comments(self, request, queryset):
        queryset.update(approved=False)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug')

