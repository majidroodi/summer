from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _



class PostCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), help_text=_('Used in the URL'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Post(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    slug = models.SlugField(max_length=200, verbose_name=_('Slug'), help_text=_('Used in the URL'))
    content = RichTextUploadingField(verbose_name=_('Content'))
    post_category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name=_('Category'))
    pub_date = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    author = models.ForeignKey(User, null=True, blank=True, verbose_name=_('Author'))
    thumbnail = models.ImageField(
        upload_to='thumbnails',
        verbose_name=_('Thumbnail')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

