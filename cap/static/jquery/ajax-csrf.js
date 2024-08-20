$.ajaxPrefilter(function(options, originalOptions, jqXHR) {

    var data = originalOptions.data;

    function isPost(method) {
        if (typeof method === 'string' || method instanceof String) {
            return method.toLowerCase() === 'post'
        }
        return false;
    }

    if (options.method === 'DELETE') {
        jqXHR.setRequestHeader("X-CSRFToken", csrf);
    }

    if (isPost(originalOptions.type) || isPost(options.type)) {
        if (typeof data === 'string' || data instanceof String) {
            data = $.deparam(data);
        }
        options.data = $.param(
            $.extend(
                {},
                data,
                {csrfmiddlewaretoken: csrf}
            ),
            true
        );
    }
});
