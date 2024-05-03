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
      'description' : forms.Textarea({'class':'form-control'}),
      'cover' : forms.FileInput({'class':'form-control'}),
      'benefits' : forms.Textarea({'class':'form-control'}),
      'variants' : forms.Textarea({'class':'form-control'}),
      'weight' : forms.TextInput({'class':'form-control'}),
    }