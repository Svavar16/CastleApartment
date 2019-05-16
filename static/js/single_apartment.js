$(document).ready(function () {

    function getThreeRandomApartments() {
        var res = "";
        let i = 1;
        var carres = "<li data-target=\"#carouselExampleCaptions\" data-slide-to=\"0\" class=\"active\"></li>\n";
        $.ajax({
            url: 'get_all_apartment_images/' + a,
            datatype: 'json',
            type: 'GET',
            success: function (data) {
                $.each(data, function (index, element) {
                    res += "<div class=\"carousel-item \">\n" +
                        "                <img alt='apartment image' width='400' height='600' src=\" " + data[index].image + " \" class=\"d-block w-100\" alt=\"...\">\n" +
                        "                </div>\n" +
                        "                \n";

                    if (i < data.length ) {
                        carres += "<li data-target=\"#carouselExampleCaptions\" data-slide-to=\"" + i +  "\"></li>\n";
                        i++;
                    }
                });

                $('#get_single_apartment_app').append(res);
                $('#carres_single_apartment_app').append(carres);

            }
        })
    }

    getThreeRandomApartments();

});