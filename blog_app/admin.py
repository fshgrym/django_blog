from django.contrib import admin
from blog_app.models import Category,Tag,Post
# Register your models here.
class Post_Admin(admin.ModelAdmin):
    list_display = ('title','body','create_time','modified_time','excerpt','category','author','views')
    date_hierarchy = 'create_time'
    list_filter = ('create_time','category')#过滤器
    ordering = ['-create_time']#文章再后台的排序方式
    search_fields = ('title','author')
    fieldsets = (None,
                 {
                     'fields':(
                         'title',
                         ('body','excerpt'),
                         ('category','author','views'),
                     ),
                 }),
    # fields = ('author','title','excerpt','body','create_time','modified_time','category')
    # filter_horizontal =('tags',)必须是多对多
    # raw_id_fields = ('tags',)必须是多对多
admin.site.register(Post,Post_Admin)
admin.site.register([Tag,Category])