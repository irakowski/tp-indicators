from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext as _


def zero_and_negative_value_validator(value):
    """Validating user input value not be equal 0 on divisible fields and and be greater than zero"""
    try:
        value = float(value)
    except ValueError:
        raise ValidationError(_('Niepoprawna wartość'))
    if float(value) <= 0.0:
        raise ValidationError(_('Ta wartość nie może być mniejsza lub równa zero'))


def negative_value_validator(value):
    """Validating user input to be greater than zero"""
    try:
        value = float(value)
    except ValueError:
        raise ValidationError(_('Niepoprawna wartosc'))
    if float(value) < 0.0:
        raise ValidationError(_('Wartości nie mogą być mniejsze lub równe zero'))


class BankForm(forms.Form):
    
    wynik_z_odsetek = forms.CharField(label=(_('Wynik z tytułu odsetek')), 
                    validators=[negative_value_validator],max_length=100,)
    srednia_wartosc_aktywow_oprocentowanych = forms.CharField(max_length=100,
                    label=(_('Średnia wartość aktywów oprocentowanych w roku obrotowym')),
                    validators=[zero_and_negative_value_validator])
    koszty_dzialania = forms.CharField(label=(_('Koszty działania')), validators=[negative_value_validator],
                    max_length=100)
    przychody = forms.CharField(label=(_('Przychody')), validators=[zero_and_negative_value_validator], 
                    max_length=100)
    zysk_strata_netto = forms.CharField(label=(_('Zysk (strata) netto')), 
                    validators=[negative_value_validator], max_length=100)
    aktywa_razem = forms.CharField(label=(_('Aktywa razem')), validators=[zero_and_negative_value_validator],
                    max_length=100)
    kapital_fundusz_wlasny = forms.CharField(label=(_('Kapitał (fundusz) własny')), 
                    validators=[zero_and_negative_value_validator], max_length=100)

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

    wynik_techniczny = forms.CharField(label=(_('Wynik techniczny')), validators=[negative_value_validator],
                                    max_length=100) 
    skladki = forms.CharField(label=(_('Składki')),validators=[zero_and_negative_value_validator],
                            max_length=100)
    zysk_strata_netto = forms.CharField(label=(_('Zysk (strata) netto')), max_length=100,
                            validators=[negative_value_validator])
    skladki_przypisane_brutto = forms.CharField(label=(_('Składki przypisane brutto')), 
                            validators=[zero_and_negative_value_validator], max_length=100)
    aktywa_razem = forms.CharField(label=(_('Aktywa razem')), validators=[zero_and_negative_value_validator],
                            max_length=100)
    kapital_fundusz_wlasny = forms.CharField(label=(_('Kapitał (fundusz) własny')), max_length=100,
                            validators=[zero_and_negative_value_validator])

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
    zysk_strata_z_dzialalnosci_operacyjnej = forms.CharField(label=(_('Zysk (strata) z działalności operacyjnej')), 
                                        validators=[negative_value_validator], max_length=100)
    
    przychody_netto = forms.CharField(label=(_('Przychody netto ze sprzedaży i zrównane z nimi')), 
                                      validators=[negative_value_validator], max_length=100)
   
    zmiana_stanu_produktow = forms.CharField(label=(_('Zmiana stanu produktów')),
                                    validators=[negative_value_validator], max_length=100)
    koszty_swiadczen = forms.CharField(label=(_('Koszty wytworzenia świadczeń na potrzeby własne')), 
                                    validators=[negative_value_validator], max_length=100)
    pozostale_przychody_operacyjne = forms.CharField(label=(_('Pozostałe przychody operacyjne')),
                                    validators=[negative_value_validator])
    zysk_strata_brutto = forms.CharField(label=(_('Zysk (strata) brutto')),
                                    validators=[negative_value_validator])
    przychody_finansowe = forms.CharField(label=(_('Przychody finansowe')), 
                                    validators=[negative_value_validator])
    zysk_strata_netto = forms.CharField(label=(_('Zysk (strata) netto')), 
                                    validators=[negative_value_validator])
    aktywa_razem = forms.CharField(label=(_('Aktywa razem')), validators=[zero_and_negative_value_validator])
    kapital_fundusz_wlasny = forms.CharField(label=(_('Kapitał (fundusz) własny')), 
                                    validators=[zero_and_negative_value_validator])

    def clean(self):
        przychody = self.cleaned_data.get('przychody_netto')
        zmiana = self.cleaned_data.get('zmiana_stanu_produktow')
        koszty = self.cleaned_data.get('koszty_swiadczen')
        pozostale = self.cleaned_data.get('pozostale_przychody_operacyjne')
        przychody_finansowe = self.cleaned_data.get('przychody_finansowe')
        result = float(przychody) - float(zmiana) - float(koszty) + float(pozostale)
        result2 = result + float(przychody_finansowe)
        if result == 0.0:
            raise ValidationError(_('Proszę sprawdzić dane wejściowe. Wprowadzone dane nie pozwalają na prawidłowe obliczenie wskaźników'))
        if result2 == 0.0:
            raise ValidationError(_('Proszę sprawdzić dane wejściowe. Wprowadzone dane nie pozwalają na prawidłowe obliczenie wskaźników'))
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
    
    zysk_strata_z_dzialalnosci_operacyjnej = forms.CharField(label=(_('Zysk (strata) z działalności operacyjnej')),
                                        validators=[negative_value_validator], max_length=100)
    przychody_netto = forms.CharField(label=(_('Przychody netto ze sprzedaży produktów, towarów i materiałów')),
                                    validators=[negative_value_validator], max_length=100)
    pozostale_przychody_operacyjne = forms.CharField(label=(_('Pozostałe przychody operacyjne')), 
                                    validators=[negative_value_validator], max_length=100)
    zysk_strata_brutto = forms.CharField(label=(_('Zysk (strata) brutto')), 
                                    validators=[negative_value_validator], max_length=100)
    przychody_finansowe = forms.CharField(label=(_('Przychody finansowe')), 
                                    validators=[negative_value_validator], max_length=100)
    zysk_strata_netto = forms.CharField(label=(_('Zysk (strata) netto')), 
                                    validators=[negative_value_validator], max_length=100)
    aktywa_razem = forms.CharField(label=(_('Aktywa razem')), max_length=100,
                                    validators=[zero_and_negative_value_validator])
    kapital_fundusz_wlasny = forms.CharField(label=(_('Kapitał (fundusz) własny')), max_length=100, 
                                    validators=[zero_and_negative_value_validator])

    def clean(self):
        przychody = self.cleaned_data.get('przychody_netto')
        pozostale = self.cleaned_data.get('pozostale_przychody_operacyjne')
        
        przychody_finansowe = self.cleaned_data.get('przychody_finansowe')
        
        result = float(przychody) + float(pozostale)
        result2 = result + float(przychody_finansowe)
        if result == 0.0:
            raise ValidationError(_('Proszę sprawdzić dane wejściowe. Wprowadzone dane nie pozwalają na prawidłowe obliczenie wskaźników'))
        if result2 == 0.0:
            raise ValidationError(_('Proszę sprawdzić dane wejściowe. Wprowadzone dane nie pozwalają na prawidłowe obliczenie wskaźników'))
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