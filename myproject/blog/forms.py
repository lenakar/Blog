# -*- coding: utf-8 -*-
from django import forms
from blog.models import Blog

class CreatBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
