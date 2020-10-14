from django import forms
from django.forms import widgets
from . import models
from django_countries.fields import CountryField


class clsSearchForm(forms.Form):

    #   required=False 은
    #   Djaneiro - Django Snippets 사용하면서 코드 자동완성되는 부분이므로
    #   굳이 지우지 않고 진행

    arrRoom_types = forms.ModelChoiceField(
        required=False,
        empty_label="Any kind",
        queryset=models.clsRoom.objects.all(),
    )
    arrCountry = CountryField(default="KR").formfield()

    varCity = forms.CharField(
        initial="Anywhere",
        max_length=20,
        required=False,
    )
    varPrice = forms.IntegerField(required=False)
    varGuests = forms.IntegerField(
        required=False,
        help_text="how meny peoples?",
    )
    varBedrooms = forms.IntegerField(required=False)
    varBed = forms.IntegerField(required=False)
    varBaths = forms.IntegerField(required=False)

    varInstant_book = forms.BooleanField(required=False)
    varSuperhost = forms.BooleanField(required=False)

    arrAmenities = forms.ModelMultipleChoiceField(
        queryset=models.clsAmenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    arrFacilities = forms.ModelMultipleChoiceField(
        queryset=models.clsFacility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    arrHouse_rules = forms.ModelMultipleChoiceField(
        queryset=models.clsHouseRule.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
