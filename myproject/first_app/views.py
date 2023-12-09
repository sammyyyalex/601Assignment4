from django import forms
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class BillForm(forms.Form):
    subtotal = forms.DecimalField(label='Subtotal',widget=forms.TextInput(attrs={'placeholder': 'Enter subtotal'}))
    tipPercentage = forms.DecimalField(label='Tip Percentage',widget=forms.TextInput(attrs={'placeholder': 'Enter tip percentage'}))

def calculate_tip(request):
    totalAmount = None
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            subtotal = form.cleaned_data['subtotal']
            tipPercentage = form.cleaned_data['tipPercentage']
            tipAmount = (tipPercentage / 100) * subtotal
            totalAmount = round(subtotal + tipAmount, 2)

    else:
        form = BillForm()

    return render(request, 'index.html', {'form': form, 'totalAmount': totalAmount})

def index(request):
   my_dict = {'insert_me':"Hello I am from views.py!"}
   return render (request, 'index.html', context=my_dict)