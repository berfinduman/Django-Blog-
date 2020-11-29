
from django import forms
from .models import Article

class Addarticle(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title", "content","article_image"]