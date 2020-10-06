from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.
from .forms import BankForm, ZakladForm, InnaCalculationForm, InnaPorownawczaForm


class TpForm(generic.TemplateView):
    template_name = 'records/form.html'
    extra_context = {'bank_form': BankForm, 
                    'zaklad_form': ZakladForm, 
                    'calculation_form': InnaCalculationForm,
                    'comparison_form': InnaPorownawczaForm}


class BankFormView(generic.FormView):
    form_class = BankForm
    template_name = 'records/bank-form.html'

    def post(self, request, *args, **kwargs):
        """
        Handle POST requests: instantiate a form instance with the passed
        POST variables and then check if it's valid.
        """
        form = self.get_form()
        if form.is_valid():
            print(form.data)
            return self.form_valid(form)
        else:
            print(form.errors)
            return self.form_invalid(form)
    
    def form_valid(self, form):
        context = {}
        wynik = form.cleaned_data.get("wynik_z_odsetek")
        context['wynik'] = wynik
        srednia = form.cleaned_data.get("srednia_wartosc_aktywow_oprocentowanych")
        context['srednia'] = srednia
        koszty = form.cleaned_data.get('koszty_dzialania')
        context['koszty'] = koszty
        przychody = form.cleaned_data.get("przychody")
        context['przychody'] = przychody
        zysk_strata_netto = form.cleaned_data.get("zysk_strata_netto")
        context['zysk_strata_netto'] = zysk_strata_netto
        aktywa_razem = form.cleaned_data.get("aktywa_razem")
        context['aktywa_razem'] = aktywa_razem
        kapital_fundusz_wlasny = form.cleaned_data.get("kapital_fundusz_wlasny")
        context['kapital_fundusz_wlasny'] = kapital_fundusz_wlasny
        marza_odsetkowa_netto = (float(wynik)/float(srednia))*100
        context['marza_odsetkowa_netto'] = round(marza_odsetkowa_netto, 3)
        koszty_dochody = (float(koszty)/float(przychody))*100
        context['koszty_dochody'] = round(koszty_dochody, 3)
        rentownosc_aktywow = (float(zysk_strata_netto)/float(aktywa_razem)) *100
        context['rentownosc_aktywow'] = round(rentownosc_aktywow, 3)
        rentownosc_kapitalu_wlasnego  = (float(zysk_strata_netto)/float(kapital_fundusz_wlasny)) *100
        context['rentownosc_kapitalu_wlasnego'] = round(rentownosc_kapitalu_wlasnego, 3)
        
        return render(self.request, self.template_name, context)


class ZakladFormView(generic.FormView):
    template_name = 'records/zaklad-form.html'
    form_class = ZakladForm

    def form_valid(self, form):
        context = dict()
        wynik_techniczny = form.cleaned_data.get('wynik_techniczny')
        context['wynik_techniczny'] = wynik_techniczny 
        skladki = form.cleaned_data.get('skladki')
        context['skladki'] = skladki
        zysk_strata_netto = form.cleaned_data.get('zysk_strata_netto')
        context['zysk_strata_netto'] = zysk_strata_netto
        skladki_przypisane_brutto = form.cleaned_data.get('skladki_przypisane_brutto')
        context['skladki_przypisane_brutto'] = skladki_przypisane_brutto
        aktywa_razem = form.cleaned_data.get('aktywa_razem')
        context['aktywa_razem'] = aktywa_razem
        kapital_fundusz_wlasny = form.cleaned_data.get('kapital_fundusz_wlasny')
        context['kapital_fundusz_wlasny'] = kapital_fundusz_wlasny

        rentownosc_dzialalnosci_technicznej = (float(wynik_teczniczny)/ float(skladki)) *100
        context['rentownosc_dzialalnosci_technicznej'] = round(rentownosc_dzialalnosci_technicznej, 3)
        rentownosc_sprzedazy = (float(zysk_strata_netto) / float(skladki_przypisane_brutto)) *100
        context['rentownosc_sprzedazy'] = round(rentownosc_sprzedazy, 3)
        rentownosc_aktywow = (float(zysk_strata_netto) / float(aktywa_razem)) *100
        context['rentownosc_aktywow'] = round(rentownosc_aktywow, 3)
        rentownosc_kapitalu_wlasnego = (float(zysk_strata_netto) / float(kapital_fundusz_wlasny)) *100
        context['rentownosc_kapitalu_wlasnego'] = round(rentownosc_kapitalu_wlasnego, 3)
        return render(request, self.template_name, context)


class ComparisonFormView(generic.FormView):
    template_name = 'records/comparison-form.html'
    form_class = InnaPorownawczaForm

    def form_valid(self, form):
        context = dict()
        zysk_strata_z_dzialalnosci_operacyjnej = form.cleaned_data.get('zysk_strata_z_dzialalnosci_operacyjnej')
        context['zysk_strata_z_dzialalnosci_operacyjnej'] = zysk_strata_z_dzialalnosci_operacyjnej
        
        przychody_netto = form.cleaned_data.get('przychody_netto')
        context['przychody_netto'] = przychody_netto

        zmiana_stanu_produktow = form.cleaned_data.get('zmiana_stanu_produktow')
        context['zmiana_stanu_produktow'] = zmiana_stanu_produktow

        koszty_swiadczen = form.cleaned_data.get('koszty_swiadczen')
        context['koszty_swiadczen'] = koszty_swiadczen

        pozostale_przychody_operacyjne = form.cleaned_data.get('pozostale_przychody_operacyjne')
        context['pozostale_przychody_operacyjne'] =pozostale_przychody_operacyjne
        zysk_strata_brutto = form.cleaned_data.get('zysk_strata_brutto')
        context['zysk_strata_brutto'] = zysk_strata_brutto

        przychody_finansowe = form.cleaned_data.get('przychody_finansowe')
        context['przychody_finansowe'] = przychody_finansowe

        zysk_strata_netto = form.cleaned_data.get('zysk_strata_netto')
        context['zysk_strata_netto'] = zysk_strata_netto

        aktywa_razem = form.cleaned_data.get('aktywa_razem')
        context['aktywa_razem'] = aktywa_razem
        kapital_fundusz_wlasny = form.cleaned_data.get('kapital_fundusz_wlasny')
        context['kapital_fundusz_wlasny'] = kapital_fundusz_wlasny

        marza_operacyjna = (float(zysk_strata_z_dzialalnosci_operacyjnej)/(float(przychody_netto)-float(zmiana_stanu_produktow) - float(koszty_swiadczen) + float(pozostale_przychody_operacyjne)))*100
        context['marza_operacyjna'] = round(marza_operacyjna, 3)
        
        marza_zysku_brutto = (float(zysk_strata_brutto) /(float(przychody_netto)-float(zmiana_stanu_produktow)-float(koszty_swiadczen)+float(pozostale_przychody_operacyjne)+float(przychody_finansowe)))*100
        context['marza_zysku_brutto'] = round(marza_zysku_brutto, 3)

        rentownosc_aktywow = (float(zysk_strata_netto)/float(aktywa_razem))*100
        context['rentownosc_aktywow'] = rentownosc_aktywow

        rentownosc_kapitalu_wlasnego = (float(zysk_strata_netto) / float(kapital_fundusz_wlasny))*100
        context['rentownosc_kapitalu_wlasnego'] = rentownosc_kapitalu_wlasnego
        return render(self.request, self.template_name, context)        


class CalculationFormView(generic.FormView):
    template_name = 'records/calculation-form.html'
    form_class = InnaCalculationForm

    def form_valid(self, form):
        context = dict()
        zysk_strata_z_dzialalnosci_operacyjnej = form.cleaned_data.get('zysk_strata_z_dzialalnosci_operacyjnej')
        context['zysk_strata_z_dzialalnosci_operacyjnej'] = zysk_strata_z_dzialalnosci_operacyjnej
        
        przychody_netto = form.cleaned_data.get('przychody_netto')
        context['przychody_netto'] = przychody_netto

        pozostale_przychody_operacyjne = form.cleaned_data.get('pozostale_przychody_operacyjne')
        context['pozostale_przychody_operacyjne'] =pozostale_przychody_operacyjne
        
        zysk_strata_brutto = form.cleaned_data.get('zysk_strata_brutto')
        context['zysk_strata_brutto'] = zysk_strata_brutto

        przychody_finansowe = form.cleaned_data.get('przychody_finansowe')
        context['przychody_finansowe'] = przychody_finansowe

        zysk_strata_netto = form.cleaned_data.get('zysk_strata_netto')
        context['zysk_strata_netto'] = zysk_strata_netto

        aktywa_razem = form.cleaned_data.get('aktywa_razem')
        context['aktywa_razem'] = aktywa_razem
        kapital_fundusz_wlasny = form.cleaned_data.get('kapital_fundusz_wlasny')
        context['kapital_fundusz_wlasny'] = kapital_fundusz_wlasny

        marza_operacyjna = (float(zysk_strata_z_dzialalnosci_operacyjnej)/(float(przychody_netto) + float(pozostale_przychody_operacyjne)))*100
        context['marza_operacyjna'] = round(marza_operacyjna, 3)
        
        marza_zysku_brutto = (float(zysk_strata_brutto) /(float(przychody_netto)+float(pozostale_przychody_operacyjne)+float(przychody_finansowe)))*100
        context['marza_zysku_brutto'] = round(marza_zysku_brutto, 3)

        rentownosc_aktywow = (float(zysk_strata_netto)/float(aktywa_razem))*100
        context['rentownosc_aktywow'] = rentownosc_aktywow

        rentownosc_kapitalu_wlasnego = (float(zysk_strata_netto) / float(kapital_fundusz_wlasny))*100
        context['rentownosc_kapitalu_wlasnego'] = rentownosc_kapitalu_wlasnego
        return render(self.request, self.template_name, context)        