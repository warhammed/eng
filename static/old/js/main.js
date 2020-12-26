$(document).ready( function() {
    var uniqueId = false;
    $(document).on('click', 'div.widget-config i', function(){
        var widgetid = ($(this).attr('id')).substring(7);
        var csrfToken = $('meta[name=\"csrf-token\"]').attr('content');
        $.ajax({
            type: 'post',
            dataType: 'json',
            data: {id : widgetid, _csrf : csrfToken, todo : 'showForm'},
            url: $(this).data('href')
        }).done(function( data ) {
            if (data.status == 'error') {
                alert(yii.t('Error in displaying information'));
            }else{
                uniqueId = (data.uniqueId) ? data.uniqueId : false;
                $('#widget-config-modal .modal-inner').html(data.content);
                $('#widget-config-modal').addClass(uniqueId);
                $('#widget-config-modal').modal('show');
                if (uniqueId) {
                    $(document).trigger(uniqueId+'Init'); //Do something in modal init in themes(e.g. utproIT)
                }
            }
        });
    });
    $(document).on('click', 'button#submit-widget-config', function(){

        if (uniqueId) {
            $(document).trigger(uniqueId+'BeforeSave'); //Do something before save widget configs in themes(e.g. utproIT)
        }
        if (!validateUrls()) {
            alert(yii.t('The url is not valid\n (for example : https://t.me/epage_ir)'));
        } else{
            $('#widget-config-modal .modal-inner form').submit();
        }
    });

    function validateUrls(){
        var validate = true;
        var urls = $('#widget-config-modal .modal-inner form input');
        urls.each(function(){
            if($(this).attr("type") == "url" && $(this).val() && !this.validity.valid){
                validate= false;
                return false;
            }
        });
        return validate;
    }

    $(document).on('submit', '#widget-config-modal .modal-inner form', function(event){
        event.preventDefault();
        formData = $(this).serializeArray();
        formData.push({name:'todo', value:'submitForm'});
        $.ajax({
            url: $(this).attr('action'),
            type: 'post',
            dataType: 'json',
            data: $.param(formData),
        }).done(function( data ) {
            if (data.status == 'success') {
                $('#widget-config-modal').modal('hide');
                alert(yii.t('Settings saved successfully.'));
                location.reload();
            }
        });
        return false;
    });

    $('#widget-config-modal').on('hidden.bs.modal', function(e) {
        $(this).removeClass(uniqueId);
    });
});
