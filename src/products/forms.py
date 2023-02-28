from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows": 20,
                "cols": 120
            }
        )
    )
    description = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Description"}))
    price = forms.DecimalField(initial=200)
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']
        
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("invalid title")

class RawProductForm(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows": 20,
                "cols": 120
            }
        )
    )
    description = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Description"}))
    price = forms.DecimalField(initial=200)