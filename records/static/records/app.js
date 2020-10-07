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
   /* $('input[type="text"]').on('change, keyup', function() {
        var currentInput = $(this).val();
        var fixedInput = currentInput.replace(/[A-Za-z!@#$%;^+&"-*</\]\{}|`_\\~[:>=?+'()]/g, '');
        fixedInput = fixedInput.replace(/[,]/g, '.');
        $(this).val(fixedInput);
    }) */
});

