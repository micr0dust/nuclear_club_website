from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Message(models.Model):
    user = models.CharField("姓名", max_length=50)
    subject = models.CharField("主旨", max_length=200)
    post_choice = (('new', '公告'),('share', '分享'), ('info', '資訊'), ('practice', '梗圖'), ('problem', '問題'), ('other', '其他'))
    post_typel = models.CharField(max_length=30, choices=post_choice, default='new')
    content = RichTextField("內容")
    publication_date = models.DateTimeField("留言日期", auto_now_add=True)

    def __str__(self):
        return self.subject