from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Category,Tag
from comments.forms import CommentForm
import markdown
from django.views.generic import ListView,DetailView
class IndexView(ListView):
    model = Post
    template_name = 'blog_app/index.html'
    context_object_name = 'post_list'
    paginate_by = 3
# def index(request):
#     post_list=Post.objects.all().order_by('-create_time')#-create_time是新文章排在前面
#     return render(request,'blog_app/index.html',context={'post_list':post_list})

class ArtucleView(IndexView):
    def get_queryset(self):
        return super(ArtucleView, self).get_queryset().filter(create_time__year=self.kwargs.get('year'),
                                    create_time__month=self.args.get('month'))
# def archives(request, year, month):
#     post_list = Post.objects.filter(create_time__year=year,
# #                                     create_time__month=month
#                                     )
#     return render(request, 'blog_app/index.html', context={'post_list': post_list})
# def detail(request,pk):#详情页面链接
#     post=get_object_or_404(Post,pk=pk)#不存在就直接报404
#     post.increase_views()
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',#代码高亮
#                                       'markdown.extensions.toc',
#                                   ])
#     form=CommentForm()
#     comment_list=post.comment_set.all()
#     context={
#         'post':post,
#         'form':form,
#         'comment_list':comment_list
#     }
#     return render(request,'blog_app/detail.html',context=context)
class PostDatailView(DetailView):
    model = Post
    template_name = 'blog_app/detail.html'
    context_object_name = 'post'

    def get(self,request,*args,**kwargs):
        response=super(PostDatailView, self).get(request,*args,**kwargs)
        self.object.increase_views()
        return response

    def get_object(self, queryset=None):
        post=super(PostDatailView, self).get_object(queryset=None)
        post.body=markdown.markdown(post.body,
                    extensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                'markdown.extensions.toc',
                    ])
        return post
    def get_context_data(self, **kwargs):
        context=super(PostDatailView, self).get_context_data(**kwargs)
        form=CommentForm()
        comment_list=self.object.comment_set.all()
        context.update(
            {
                'form':form,
                'comment_list':comment_list
            }
        )
        return context

class CategoryView(IndexView):
    def get_queryset(self):
        cate=get_object_or_404(Category,pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)
# def category(request,pk):#分类页面链接
#     cate=get_object_or_404(Category,pk=pk)
#     post_list=Post.objects.filter(category=cate)
#     return render(request,'blog_app/index.html',context={'post_list':post_list})

class TagsView(IndexView):
    def get_queryset(self):
        cate=get_object_or_404(Tag,name=self.kwargs.get('tag'))
        return super(TagsView, self).get_queryset().filter(tags=cate)


# def tags(request,tag):#标签页面链接
#     tag=get_object_or_404(Tag,name=tag)
#     post_list=Post.objects.filter(tags=tag)
#     return render(request,'blog_app/index.html',context={'pose_list':post_list})
