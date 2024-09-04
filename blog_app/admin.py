from django.contrib import admin
from .models import User, Post, Comments
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title','content','views')

admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('writer', 'contents','date')
admin.site.register(Comments, CommentAdmin)

admin.site.register(User)
