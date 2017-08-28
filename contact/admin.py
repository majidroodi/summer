from django.contrib import admin
from .models import Letter, LetterSubject

class LetterAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'client_email', 'letter_subject', 'postage_date']
    list_filter = ['postage_date', 'letter_subject']


class LetterSubjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_editable = ['title']
    list_display_links = None


admin.site.register(Letter, LetterAdmin)
admin.site.register(LetterSubject, LetterSubjectAdmin)
