# yourapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Render the 'home.html' template
    return render(request, 'home.html')

def another_view(request):
    # You can pass data to the template using a dictionary
    context = {'message': 'This is another view!'}
    return render(request, 'another_template.html', context)
