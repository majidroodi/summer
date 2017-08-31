from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels

class LetterSubject(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Subject Title'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Subject')
        verbose_name_plural = _('Subjects')


class Letter(models.Model):
    client_name = models.CharField(max_length=50, verbose_name=_('Name'))
    client_email = models.EmailField(max_length=200, verbose_name=_('Email'))
    client_phone = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('Phone Number'))
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    letter_subject = models.ForeignKey(LetterSubject, on_delete=models.CASCADE, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('Message'))
    postage_date = jmodels.jDateField(auto_now_add=True, verbose_name=_('Postage Date'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Letter')
        verbose_name_plural = _('Letters')
