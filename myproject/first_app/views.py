from django import forms
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class BillForm(forms.Form):
    subtotal = forms.DecimalField(label='Subtotal')
    tipPercentage = forms.DecimalField(label='Tip Percentage')

def calculate_tip(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            subtotal = form.cleaned_data['subtotal']
            tipPercentage = form.cleaned_data['tipPercentage']
            tipAmount = (tipPercentage / 100) * subtotal
            totalAmount = subtotal + tipAmount
            return render(request, 'index.html', {'totalAmount': totalAmount})
    else:
        form = BillForm()

    return render(request, 'first_app/index.html', {'form': form})

#def index(request):
#    my_dict = {'insert_me':"Hello I am from views.py!"}
#    return render (request, 'index.html', context=my_dict)