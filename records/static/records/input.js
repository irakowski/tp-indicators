$(function(){
    $('input[type="text"]').on('change, keyup', function() {
        var currentInput = $(this).val();
        var fixedInput = currentInput.replace(/[A-Za-z!@#$%;^+&"-*/<\]\{}|`_\\~[:>=?+'()]/g, '');
        fixedInput = fixedInput.replace(/[,]/g, '.');
        $(this).val(fixedInput);
    });
});