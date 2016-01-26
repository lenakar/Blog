# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    content = models.TextField(u'Содержимое')
    creat_date = models.DateTimeField(u'Дата создания',auto_now_add=True)
    class Meta:
        db_table = "blog"
#    def __unicode__(self):
#        return self.title
