from django.forms import ModelForm
from django import forms
# from perpustakaan.models import Buku
from reviews.models import Product

class FormProduct(ModelForm):
  class Meta:
    model = Product
    fields = '__all__'

    widgets = {
      'name' : forms.TextInput({'class':'form-control'}),
      'description' : forms.TextInput({'class':'form-control'}),
    #   'penerbit' : forms.TextInput({'class':'form-control'}),
    #   'jumlah' : forms.NumberInput({'class':'form-control'}),
    #   'kelompok_id' : forms.Select({'class':'form-control'}),
    }