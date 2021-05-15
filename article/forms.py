from django import forms
from django.db.models import fields
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title','content','article_image']
