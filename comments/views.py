from django.shortcuts import render,redirect,get_object_or_404
from blog_app.models import Post

from .models import Comment
from .forms import CommentForm
from .models import Comment
def post_comment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():#检查数据是否合法
            # comment=form.save(commit=False)#commit=Flase的作用是仅仅利用表单的数据生成comment模型类的实例
            # comment.post=post
            # comment.save()#save是保存在数据库
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            url=form.cleaned_data['url']
            text=form.cleaned_data['text']
            comment=Comment.objects.create(name=name,email=email,url=url,text=text,post=post)
            comment.save()
            return redirect(post)
        else:#如果不合法,重新渲染详情页，并且渲染表单信息
            comment_list=post.comment_set.all()
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list, }
            return render(request,'blog_app/detail.html',context=context)
    #不是post请求，说明用户没有提交数据，重定向到文章详情页
    return redirect(post)#redirect 既可以接收一个 URL 作为参数，也可以接收一个模型的实例作为参数（例如这里的 post）。如果接收一个模型的实例，那么这个实例必须实现了 get_absolute_url 方法，这样 redirect 会根据 get_absolute_url 方法返回的 URL 值进行重定向


#留言
def Contact(request):
    return render(request,'blog_app/contact.html')