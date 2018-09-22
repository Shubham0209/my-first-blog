from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('text', 'title', 'published_date')