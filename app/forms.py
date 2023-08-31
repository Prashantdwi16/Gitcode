from django import forms
from .models import *
 #just for git


class inventoryform(forms.ModelForm):
    status=[
    ('approve','APPROVED'),
    ('pending','PENDING')
    ]
    ProductId=forms.IntegerField(label='ProductId')
    ProductName=forms.CharField(label="ProductName",max_length=100)
    Vendor=forms.CharField(label="Vendor",max_length=100)
    MRP=forms.FloatField(label="MRP")
    BatchNum=forms.IntegerField(label="BatchNum")
    BatchDate=forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    Quantity=forms.CharField(label="Quantity",max_length=100)
    status=forms.ChoiceField(choices=status, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = inventory
        fields = '__all__' 
       



       