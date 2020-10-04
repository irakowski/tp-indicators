$(function(){

	$('input[name=institution-type]').click(function () {
		$('input[name=institution-type]').removeAttr("selected");
        $(this).attr("selected", "");
        if($(this).attr("value")=="Inny podmiot"){
            $("#rzis").removeAttr('hidden');
        } else {
            $("#rzis").attr("hidden","")}
        if($(this).attr("value")=="Bank") {
            $("#bank-form").removeAttr('hidden');
        } else {
            $("#bank-form").attr("hidden", "");
        };
        if($(this).attr("value")=="Zakład ubezpieczeń / reasekuracji") {
            $("#zaklad-form").removeAttr('hidden');
        } else {
            $("#zaklad-form").attr("hidden", "");
        }
    });
    
    $("input[name='rzis-type']").click(function() {
        $("input[name='rzis-type']").removeAttr("selected");
        $(this).attr("selected", "");
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
    /*$('input[type="button"]'). {
        if($(this).attr('selected')=='selected') {
            $(this).removeClass('btn-outline-primary').addClass('btn-primary');
        } else {
            $(this).removeClass('btn-primary').addClass('btn-outline-primary');
        }
        
    });*/
});

