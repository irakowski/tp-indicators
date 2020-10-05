$(function(){

	$('input[name=institution-type]').click(function () {
        $('input[name=institution-type]').removeClass('btn-primary').addClass('btn-outline-primary');
        $(this).removeClass('btn-outline-primary').addClass('btn-primary');
        //$('input[name=institution-type]').removeAttr("selected");
        //$(this).attr("selected", "");
        if($(this).attr("value")=="Inny podmiot"){
            $("#rzis").removeAttr('hidden');
            $('#calculation-form').attr('hidden', "'");
            $('#comparison-form').attr('hidden', "");
        } else {
            $("#rzis").attr("hidden","")}
        if($(this).attr("value")=="Bank") {
            $("#bank-form").removeAttr('hidden');
            $('#calculation-form').attr('hidden', "'");
            $('#comparison-form').attr('hidden', "");
        } else {
            $("#bank-form").attr("hidden", "");
        };
        if($(this).attr("value")=="Zakład ubezpieczeń / reasekuracji") {
            $("#zaklad-form").removeAttr('hidden');
            $('#calculation-form').attr('hidden', "'");
            $('#comparison-form').attr('hidden', "");
        } else {
            $("#zaklad-form").attr("hidden", "");
        }
    });
    
    $("input[name='rzis-type']").click(function() {
        $("input[name='rzis-type']").removeClass('btn-primary').addClass('btn-outline-primary');
        $(this).removeClass('btn-outline-primary').addClass('btn-primary');
        //$("input[name='rzis-type']").removeAttr("selected");
        //$(this).attr("selected", "");
       // $("input[selected='selected']").removeClass('btn-outline-primary').addClass('btn-primary');
        if($(this).attr("value")=="Wariant porównawczy"){
            $('#comparison-form').removeAttr('hidden');
            $('#calculation-form').attr('hidden', "'");
        } else {
            $('#comparison-form').attr('hidden', "");
        }
        if($(this).attr("value")=="Wariant kalkulacyjny"){
            $('#calculation-form').removeAttr('hidden');
            $('#comparison-form').attr('hidden', "");
        }
    });
    $('input[type="text"').on('change, keyup', function() {
        var currentInput = $(this).val();
        var fixedInput = currentInput.replace(/[A-Za-z!@#$%;^+&"-*/<\]\{}|`_\\~[:>=?+'()]/g, '');
        fixedInput = fixedInput.replace(/[,]/g, '.');
        $(this).val(fixedInput);
    })
   /* $("#zaklad-calculation").click(function(){
        $('#zaklad-result').removeAttr('hidden');
        var wynikTechnicny = Number($("#zaklad-wynik-techniczy").val());
        var skladki = Number($("#zaklad-skladki").val());
        var rentownosc = (wynikTechnicny / skladki) * 100
        $("#rentownosc-techniczna").html( "Rentownosc działalności technicznej wynosi: "+ rentownosc.toFixed(3) +"%" );

        var zyskStrata = Number($("#zaklad-zysk").val());
        var skladkiBrutto = Number($("#zaklad-skladki-brutto").val())
        var sprzedaza = (zyskStrata / skladkiBrutto) * 100;
        $("#rentownosc-sprzedazy").html( "Rentownosc sprzedazy wynosi: "+ sprzedaza.toFixed(3) +"%" );

        var aktywaRazem = Number($("#zaklad-aktywa-razem").val())
        var aktywa = (zyskStrata / aktywaRazem) * 100;
        $("#rentownosc-aktywow").html( "Rentownosc aktywow wynosi: "+ aktywa.toFixed(3) +"%" );

        var kapitalValue = Number($("#zaklad-kapital").val())
        var kapital = (zyskStrata / kapitalValue) * 100;
        $("#rentownosc-kapitalu").html( "Rentownosc kapitału własnego wynosi : "+ kapital.toFixed(3) +"%" )
    });
    */
});

