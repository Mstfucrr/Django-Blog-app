from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ForeignKey


# Create your models here.

class Article(models.Model):

    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    title = models.CharField(max_length=50,verbose_name="Başlık")
    content = RichTextField(verbose_name="İçerik")
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye Fotoğraf Ekle")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date'] # son eklenenden ilke eklenene doğru sıralar Bu işlem sonrası makemigration ve akabinde migrate yapılmalı

class Comment(models.Model):
    article = ForeignKey(Article,on_delete=models.CASCADE,related_name="comments")
    comment_author = models.CharField(max_length=50,verbose_name="İsim")
    comment_content = models.CharField(max_length=200,verbose_name="Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']# son eklenenden ilke eklenene doğru sıralar Bu işlem sonrası makemigration ve akabinde migrate yapılmalı