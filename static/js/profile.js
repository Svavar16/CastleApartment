$(document).ready(function () {
    function getsearchhistory5newest() {
        var pathname = window.location.pathname;
        var pathvar = pathname.charAt(pathname.length - 1);

        $.ajax({
            url: 'show_history/',
            datatype: 'Json',
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    return `<h3>${d.searchItem}</h3>`
                });
                $('#get_search_history_app').html(newHTML.join(''))
            }
        })
    }

    function getsearchhistory5newestbyid(id) {
        var pathname = window.location.pathname;
        var pathvar = pathname.charAt(pathname.length - 1)

        $.ajax({
            url: id + '/show_history/',
            datatype: 'Json',
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    return `<h3>${d.searchItem}</h3>`
                });
                $('#get_search_history_app').html(newHTML.join(''))
            }
        })
    }

})