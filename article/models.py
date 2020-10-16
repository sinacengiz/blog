from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="yazar")
    title=models.CharField(max_length=50,verbose_name="başlık")
    content=RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="eklenme tarihi")
    article_image=models.FileField(blank=True,null=True,verbose_name="foto ekle")
    def __str__(self):#author bilsinden almak istiyorsam da self.author derim
        return self.title
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="isim")
    comment_content=models.CharField(max_length=200,verbose_name="yorum")
    comment_datte=models.DateTimeField(auto_now_add=True)