from django import forms
from . import models


class clsSearchform(forms.Form):

    #   required=False 은
    #   Djaneiro - Django Snippets 사용하면서 코드 자동완성되는 부분이므로
    #   굳이 지우지 않고 진행

    varCity = forms.CharField(initial="Anywhere", max_length=20, required=False)
    varPrice = forms.IntegerField(required=False)
    arrRoom_types = forms.ModelChoiceField(queryset=models.clsRoom.objects.all())
