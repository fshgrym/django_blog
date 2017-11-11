from django.contrib import admin
from blog_app.models import Category,Tag,Post
# Register your models here.
class Post_Admin(admin.ModelAdmin):
    list_display = ('title','body','create_time','modified_time','excerpt','category','author')
admin.site.register(Post,Post_Admin)
admin.site.register([Tag,Category])