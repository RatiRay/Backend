
from django.contrib import admin

# Register your models here.
from .models import book,Post, Comment


# admin.site.register(Post)
# CUSTOMISING POST MODEL DISPLAY
admin.site.register(book)
@admin.register(Post)
class Postadmin(admin.ModelAdmin):
    list_display =('title','slug','author', 'publish','status')
    list_filter=('status','created','publish','author')
    search_fields=('title','body',)
    prepopulated_fields={'slug': ('title',)}
    raw_id_fields=('author',)
    date_hierachy= 'publish'
    ordering=('status','publish')





@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display= ('name', 'email','post','created', 'active')
    list_filter= ('active', 'created', 'update')
    search_fields= ('name', 'email', 'body')