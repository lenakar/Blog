# -*- coding: utf-8 -*-
from django import forms
from blog.models import Blog

class CreatBlogForm(forms.ModelForm):
    #title = forms.CharField(label= u'Заголовок',max_length=255)
    #content = forms.CharField(label= u'Содержимое',widget=forms.Textarea(attrs={"cols":"40", "rows":"7"}))
    class Meta:
        model = Blog
