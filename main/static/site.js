
function submit(form,url){
    var segment = form.parent();
    segment.addClass('loading');
    jQuery.ajax( url ? url : form.attr('action'),
        {
            method:form.attr('method'),
            dataType:'json',
            data:form.serializeArray(),
            success:function(result){
                var msg = form.find('.message');
                if(result['message']){
                    msg.text(result['message']);
                }
                if(result['success']){
                    msg.addClass('positive');
                    msg.removeClass('negative');
                }
                else{
                    msg.addClass('negative');
                    msg.removeClass('positive');
                }
                msg.removeClass('hidden');
            },
            error:function(e,f){
                console.error(e);
                console.error(f);
            },
            complete:function(){
                segment.removeClass('loading');
            }
        }
    );
}

jQuery(function(){
    jQuery('form').submit(function(){
        var form = jQuery(this);
        submit(form);
        return false;
    });

    $("#logout").click(function() {
        var url = jQuery(this).attr('href');
        var form = jQuery(this).parents('form');
        console.log(form);
        console.log(url);
        submit(form,url);
        return false;
    });
});
