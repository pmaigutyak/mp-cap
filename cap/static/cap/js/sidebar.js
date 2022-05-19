
(function ($) {
    var $container = $('#container'),
        $toggle = $('[data-role=sidebar-toggle]'),
        cookieName = 'admin-sidebar';

    function saveState(isCollapsed) {
        $.cookie(cookieName, isCollapsed, {path: '/'});
    }

    if ($.cookie(cookieName) === 'true') {
        $container.addClass('collapsed');
    }

    $toggle.on('click', function () {
        $container.toggleClass('collapsed');
        saveState($container.hasClass('collapsed'));
    });

})(jQuery);
