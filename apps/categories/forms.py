from django import forms
from apps.categories.models import Categories


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ['title',]
