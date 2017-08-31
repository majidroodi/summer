from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django_jalali.db import models as jmodels


class PostCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    slug = models.SlugField(max_length=100, verbose_name=_('Slug'), help_text=_('Used in the URL'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class Post(models.Model):
    objects = jmodels.jManager()
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    slug = models.SlugField(max_length=200, verbose_name=_('Slug'), help_text=_('Used in the URL'))
    brief_content = models.TextField(verbose_name=_('Brief content'), null=True)
    content = RichTextUploadingField(verbose_name=_('Content'), null=True)
    post_category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name=_('Category'))
    pub_date = jmodels.jDateField(verbose_name=_('Publish date'))
    last_modified = jmodels.jDateField(auto_now=True, verbose_name=_('Modified date'))
    pub_status = models.BooleanField(default=True, verbose_name=_('Publish status'))
    author = models.ForeignKey(User, null=True, blank=True, verbose_name=_('Author'))
    thumbnail = models.ImageField(
        upload_to='thumbnails',
        verbose_name=_('Thumbnail'),
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

