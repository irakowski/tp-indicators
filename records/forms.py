from django import forms

class BankForm(forms.Form):
    
    wynik_z_odsetek = forms.CharField(max_length=100, widget=forms.TextInput())
    srednia_wartosc_aktywow_oprocentowanych = forms.CharField(max_length=100)
    koszty_dzialania = forms.CharField()
    przychody = forms.CharField()
    zysk_strata_netto = forms.CharField()
    aktywa_razem = forms.CharField()
    kapital_fundusz_wlasny = forms.CharField()

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