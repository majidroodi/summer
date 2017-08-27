from django.shortcuts import render
from .models import Letter
from .forms import LetterForm

def contact(request):
    success = False
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            form = LetterForm()
            success = True

    else:
        form = LetterForm()

    context = {
        'form': form,
        'success': success,
    }
    return render(request, 'contact/contact.html', context)
