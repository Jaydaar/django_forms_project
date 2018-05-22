from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'formapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESSFUL!")
            print("Name: {}.".format(form.cleaned_data['name']))
            print("Email: {}.".format(form.cleaned_data['email']))
            print("Text: {}.".format(form.cleaned_data['text']))

    context = {
        'form':form
    }
    return render(request, 'formapp/form_page.html', context)
