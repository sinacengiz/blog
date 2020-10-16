from django import forms
from .models import  Article
#django documentation da model forms a git
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
#sadece title ve content den input olussun istiorum diierlerini almıycam
        fields=["title","content","article_image"]