from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.urls import reverse
from DjangoUeditor.models import UEditorField
# Create your models here.
@python_2_unicode_compatible#python2.xx
class Category(models.Model):#
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='分类'
        verbose_name_plural='分类'
@python_2_unicode_compatible
class Tag(models.Model):
    name=models.CharField(max_length=100)
    class Meta:
        verbose_name='标签'
        verbose_name_plural='标签'
    def __str__(self):
        return self.name
@python_2_unicode_compatible
class Post(models.Model):
    title=models.CharField(max_length=100)
    body=UEditorField('内容', height=600, width=1000,
        default=u'', blank=True, imagePath="uploads/images/",
        toolbars='besttome', filePath='uploads/files/')
    create_time=models.DateTimeField(auto_now_add=True,editable=True)#创建时间
    modified_time=models.DateTimeField(auto_now=True,null=True)#修改时间
    excerpt=models.CharField(max_length=200,blank=True)#文章摘要
    category=models.ForeignKey(Category)#文章分类
    tags=models.ManyToManyField(Tag,blank=True)#标签
    author=models.ForeignKey(User)#继承django
    views=models.PositiveIntegerField(default=0)
    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_app:detail',kwargs={'pk':self.pk})#这里的blog_app:detail就是app_name=blog_app声明好的，不申明会报错，detail就是name
    class Meta:
        ordering=['-create_time']#指定文章排序方式
        verbose_name='文章'
        verbose_name_plural='文章'

