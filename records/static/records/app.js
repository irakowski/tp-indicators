$(function(){

	$('input[name=institution-type]').click(function () {
		$('input[name=institution-type]').removeAttr("selected");
        $(this).attr("selected", "");
        if($(this).attr("value")=="Inny podmiot"){
            $("#rzis").removeAttr('hidden');
        } else {
            $("#rzis").attr("hidden","")}
	});
});
