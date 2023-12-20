from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Cat, Dog


# Create your views here.
"""def index(request):
    

    return render(request, "display.html", context)"""
# Приведенное выше представление на основе
# функций вернет все объекты изображений из нашей базы данных по запросу.
# feedback/views.py


def feedback_view(request):
    dogs = Dog.objects.all()
    cats = Cat.objects.all()


    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FeedbackForm()
        context = {
            'cats': cats,
            'dogs': dogs,
            'form': form,
        }
    return render(request, 'feedback_form.html', context)

def success_view(request):
    return render(request, 'success.html')

def error_view(request):
    return render(request, 'error.html')
