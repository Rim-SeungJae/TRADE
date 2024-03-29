from django.contrib import admin
from list.models import Post

# Register models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','modify_dt')
    list_filter = ('modify_dt',)
    search_fields=('title','content')
    prepopulated_fields={'slug':('title',)}
