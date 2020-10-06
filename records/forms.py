from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext as _


def zero_value_validator(value):
    """Validating user input value not be equal 0 on divisible fields"""
    if float(value) == 0.0:
        raise ValidationError(_("Ta wartosc nie moze byc rowna zero"))


def negative_value_validator(value):
    """Validating user input to be greater than zero"""
    if float(value) < 0.0:
        raise ValidationError(_("Wartosci nie moga byc mniejsze od zero"))


class BankForm(forms.Form):
    
    wynik_z_odsetek = forms.CharField(max_length=100, widget=forms.TextInput, validators=[negative_value_validator])
    srednia_wartosc_aktywow_oprocentowanych = forms.CharField(max_length=100, validators=[zero_value_validator, negative_value_validator])
    koszty_dzialania = forms.CharField(validators=[negative_value_validator])
    przychody = forms.CharField(validators=[zero_value_validator,negative_value_validator])
    zysk_strata_netto = forms.CharField(validators=[negative_value_validator])
    aktywa_razem = forms.CharField(validators=[zero_value_validator, negative_value_validator])
    kapital_fundusz_wlasny = forms.CharField(validators=[zero_value_validator, negative_value_validator])

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

    wynik_techniczny = forms.CharField(validators=[negative_value_validator]) 
    skladki = forms.CharField(validators=[negative_value_validator, zero_value_validator])
    zysk_strata_netto = forms.CharField(validators=[negative_value_validator])
    skladki_przypisane_brutto = forms.CharField(validators=[negative_value_validator, zero_value_validator])
    aktywa_razem = forms.CharField(validators=[negative_value_validator, zero_value_validator])
    kapital_fundusz_wlasny = forms.CharField(validators=[negative_value_validator,zero_value_validator])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-6'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Row(
                Column('wynik_techniczny', css_class='form-group col-md-8 mb-0'),
                Column('skladki', css_class='form-group col-md-8 mb-0'),
                Column('zysk_strata_netto', css_class='form-group col-md-8 mb-0'),
                Column('skladki_przypisane_brutto', css_class='form-group col-md-8 mb-0'),
                Column('aktywa_razem', css_class='form-group col-md-8 mb-0'),
                Column('kapital_fundusz_wlasny', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Policz')
        )
    
class OtherEntityComparisonForm(forms.Form):
    zysk_strata_z_dzialalnosci_operacyjnej = forms.CharField(validators=[negative_value_validator])
    
    przychody_netto = forms.CharField(label='Przychody netto ze sprzedaży i zrównane z nimi', 
                                      validators=[negative_value_validator])
   
    zmiana_stanu_produktow = forms.CharField(validators=[negative_value_validator])
    koszty_swiadczen = forms.CharField(label='Koszty wytworzenia świadczeń na potrzeby własne', 
                                       validators=[negative_value_validator])
    pozostale_przychody_operacyjne = forms.CharField(validators=[negative_value_validator])
    zysk_strata_brutto = forms.CharField(validators=[negative_value_validator])
    przychody_finansowe = forms.CharField(validators=[negative_value_validator])
    zysk_strata_netto = forms.CharField(validators=[negative_value_validator])
    aktywa_razem = forms.CharField(validators=[negative_value_validator, zero_value_validator])
    kapital_fundusz_wlasny = forms.CharField(validators=[negative_value_validator, zero_value_validator])

    def clean(self):
        przychody = self.cleaned_data.get('przychody_netto')
        zmiana = self.cleaned_data.get('zmiana_stanu_produktow')
        koszty = self.cleaned_data.get('koszty_swiadczen')
        pozostale = self.cleaned_data.get('pozostale_przychody_operacyjne')
        przychody_finansowe = self.cleaned_data.get('przychody_finansowe')
        result = float(przychody) - float(zmiana) - float(koszty) + float(pozostale)
        result2 = result + float(przychody_finansowe)
        if result == 0.0:
            raise ValidationError(_('Prosze sprawdzic dane wyjsciowe. W wyniku kalkulacji dzielnik stanowi 0'))
        if result2 == 0.0:
            raise ValidationError(_('Prosze sprawdzic dane wyjsciowe. W wyniku kalkulacji dzielnik stanowi 0'))
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-6'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Row(
                Column('zysk_strata_z_dzialalnosci_operacyjnej', css_class='form-group col-md-8 mb-0'),
                Column('przychody_netto', css_class='form-group col-md-8 mb-0'),
                Column('zmiana_stanu_produktow', css_class='form-group col-md-8 mb-0'),
                Column('koszty_swiadczen', css_class='form-group col-md-8 mb-0'),
                Column('pozostale_przychody_operacyjne', css_class='form-group col-md-8 mb-0'),
                Column('zysk_strata_brutto', css_class='form-group col-md-8 mb-0'),
                Column('przychody_finansowe', css_class='form-group col-md-8 mb-0'),
                Column('zysk_strata_netto', css_class='form-group col-md-8 mb-0'),
                Column('aktywa_razem', css_class='form-group col-md-8 mb-0'),
                Column('kapital_fundusz_wlasny', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Policz')
        )


class OtherEntityCalculationForm(forms.Form):
    
    zysk_strata_z_dzialalnosci_operacyjnej = forms.CharField(validators=[negative_value_validator])
    przychody_netto = forms.CharField(label='Przychody netto ze sprzedaży produktów, towarów i materiałów',
                                      validators=[negative_value_validator])
    pozostale_przychody_operacyjne = forms.CharField(validators=[negative_value_validator])
    zysk_strata_brutto = forms.CharField(validators=[negative_value_validator])
    przychody_finansowe = forms.CharField(validators=[negative_value_validator])
    zysk_strata_netto = forms.CharField(validators=[negative_value_validator])
    aktywa_razem = forms.CharField(validators=[zero_value_validator, negative_value_validator])
    kapital_fundusz_wlasny = forms.CharField(validators=[zero_value_validator, negative_value_validator])

    def clean(self):
        przychody = self.cleaned_data.get('przychody_netto')
        pozostale = self.cleaned_data.get('pozostale_przychody_operacyjne')
        
        przychody_finansowe = self.cleaned_data.get('przychody_finansowe')
        
        result = float(przychody) + float(pozostale)
        result2 = result + float(przychody_finansowe)
        if result == 0.0:
            raise ValidationError(_('Prosze sprawdzic dane wyjsciowe. W wyniku kalkulacji dzielnik stanowi 0'))
        if result2 == 0.0:
            raise ValidationError(_('Prosze sprawdzic dane wyjsciowe. W wyniku kalkulacji dzielnik stanowi 0'))
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-6'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Row(
                Column('zysk_strata_z_dzialalnosci_operacyjnej', css_class='form-group col-md-8 mb-0'),
                Column('przychody_netto', css_class='form-group col-md-8 mb-0'),
                Column('pozostale_przychody_operacyjne', css_class='form-group col-md-8 mb-0'),
                Column('zysk_strata_brutto', css_class='form-group col-md-8 mb-0'),
                Column('przychody_finansowe', css_class='form-group col-md-8 mb-0'),
                Column('zysk_strata_netto', css_class='form-group col-md-8 mb-0'),
                Column('aktywa_razem', css_class='form-group col-md-8 mb-0'),
                Column('kapital_fundusz_wlasny', css_class='form-group col-md-8 mb-0'),
            ),
            Submit('submit', 'Policz')
        )