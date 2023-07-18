from django.shortcuts import render
from .models import Tutorial


def tutorial_view(request):
    my_objects = Tutorial.objects.all()
    return render(request, 'tutorial/tutorial.html', {'my_objects': my_objects})
