from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())

# 留言列表
class MessageList(ListView):
    model = Message
    ordering = ['-id']      # 以 id 欄位值由大至小反向排序

# 留言檢視
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'post_typel', 'subject', 'content']     # 僅顯示 user, post_typel, subject, content 這 4 個欄位
    success_url = '/message/'                   # 新增成功後，導向留言列表
    template_name = 'form.html'                 # 指定欲使用的頁面範本

    # 刪除留言
class MessageDelete(DeleteView):
    model = Message
    success_url = '/message/'                # 刪除成功返回留言列表
    template_name = 'confirm_delete.html'
"""
    # 修改留言
class MessageUpdate(UpdateView):
    model = Message
    success_url = '/message/'                # 刪除成功返回留言列表
    template_name = 'confirm_update.html'
"""
