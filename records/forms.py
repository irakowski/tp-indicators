from django import forms
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

def zero_value_validator(value):
    if float(value) == 0.0:
        raise ValidationError(_("Ta wartosc nie moze byc rowna zero"))

def negative_values_validator(value):
    if float(value) < 0.0:
        raise ValidationError(_("Wartosci nie moga byc mniejsze od zero"))

class BankForm(forms.Form):
    
    wynik_z_odsetek = forms.CharField(max_length=100, widget=forms.TextInput, validators=[negative_values_validator])
    srednia_wartosc_aktywow_oprocentowanych = forms.CharField(max_length=100, validators=[zero_value_validator, negative_values_validator])
    koszty_dzialania = forms.CharField(validators=[negative_values_validator])
    przychody = forms.CharField(validators=[zero_value_validator,negative_values_validator])
    zysk_strata_netto = forms.CharField(validators=[negative_values_validator])
    aktywa_razem = forms.CharField(validators=[zero_value_validator, negative_values_validator])
    kapital_fundusz_wlasny = forms.CharField(validators=[zero_value_validator, negative_values_validator])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-6'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Row(
                Column('wynik_z_odsetek', css_class='form-group col-md-8 mb-0'),
                Column('srednia_wartosc_aktywow_oprocentowanych', css_class='form-group col-md-8 mb-0'),
                Column('koszty_dzialania', css_class='form-group col-md-8 mb-0'),
                Column('przychody', css_class='form-group col-md-8 mb-0'),
                Column('zysk_strata_netto', css_class='form-group col-md-8 mb-0'),
                Column('aktywa_razem', css_class='form-group col-md-8 mb-0'),
                Column('kapital_fundusz_wlasny', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Policz')
        )

class ZakladForm(forms.Form):

    wynik_techniczny = forms.CharField() 
    skladki = forms.CharField()
    zysk_strata_netto = forms.CharField()
    skladki_przypisane_brutto = forms.CharField()
    aktywa_razem = forms.CharField()
    kapital_fundusz_wlasny = forms.CharField()
    
class InnaPorownawczaForm(forms.Form):
    zysk_strata_z_dzialalnosci_operacyjnej = forms.CharField()
    przychody_netto = forms.CharField(label='Przychody netto ze sprzedaży i zrównane z nimi')
    zmiana_stanu_produktow = forms.CharField()
    koszty_swiadczen = forms.CharField(label='Koszty wytworzenia świadczeń na potrzeby własne')
    pozostale_przychody_operacyjne = forms.CharField()
    zysk_strata_brutto = forms.CharField()
    przychody_finansowe = forms.CharField()
    zysk_strata_netto = forms.CharField()
    aktywa_razem = forms.CharField()
    kapital_fundusz_wlasny = forms.CharField()


class InnaCalculationForm(forms.Form):
    
    zysk_strata_z_dzialalnosci_operacyjnej = forms.CharField()
    przychody_nettow = forms.CharField(label='Przychody netto ze sprzedaży produktów, towarów i materiałów')
    pozostale_przychody_operacyjne = forms.CharField()
    zysk_strata_brutto = forms.CharField()
    przychody_finansowe = forms.CharField()
    zysk_strata_netto = forms.CharField()
    aktywa_razem = forms.CharField()
    kapital_fundusz_własny = forms.CharField()