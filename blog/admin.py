from django.contrib import admin

# Register your models here.
from .models import Post

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'covers' , 'slug', 'pubdate', 'category', 'status')
    list_filter = ('category', 'status')
    search_fields = ('title', 'body')
    ordering = ['status', 'pubdate']


admin.site.register(Post, BookAdmin)
