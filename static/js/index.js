$(document).ready(function () {

    function getThreeRandomApartments() {
        var res = "";
        let i = 1;
        var carres = "<li data-target=\"#carouselExampleCaptions\" data-slide-to=\"0\" class=\"active\"></li>\n";
        $.ajax({
            url: 'get_three_random_apartments/',
            datatype: 'json',
            type: 'GET',
            success: function (data) {
                $.each(data, function (index, element) {
                    if (i == 1) {
                        res += "<div class=\"carousel-item active \">\n" +
                        "<a href='/apartments/" + data[index].id + "'>" +
                        "                <img alt='apartment image' width='400' height='600' src=\" " + data[index].first_image + " \" class=\"d-block w-100\" alt=\"...\">\n" +
                        "                <div class=\"carousel-caption d-none d-md-block\" style='background-color: rgba(0,0,0,0.5)'>\n" +
                        "              <h5>" + data[index].locationID_streetname + " " + data[index].locationID_houseNum + "</h5>\n" +
                        "              <p>" + data[index].description + "</p>\n" +
                        "                </div>\n" +
                        "                </div>\n" +
                        "</a>" +
                        "                \n";
                    }
                    else {
                        res += "<div class=\"carousel-item \">\n" +
                        "<a href='/apartments/" + data[index].id + "'>" +
                        "                <img alt='apartment image' width='400' height='600' src=\" " + data[index].first_image + " \" class=\"d-block w-100\" alt=\"...\">\n" +
                        "                <div class=\"carousel-caption d-none d-md-block\" style='background-color: rgba(0,0,0,0.5)'>\n" +
                        "              <h5>" + data[index].locationID_streetname + " " + data[index].locationID_houseNum + "</h5>\n" +
                        "              <p>" + data[index].description + "</p>\n" +
                        "                </div>\n" +
                        "                </div>\n" +
                        "</a>" +
                        "                \n";
                    }


                    if (i < data.length ) {
                        carres += "<li data-target=\"#carouselExampleCaptions\" data-slide-to=\"" + i +  "\"></li>\n";
                        i++;
                    }
                });

                $('#get_three_elements_app').append(res);
                $('#carres_app').append(carres);

            }
        })
    }

    function getNewestApartment() {
        var res = "";
        $.ajax({
            url: 'get_newest_apartment/',
            datatype: 'json',
            type: 'GET',
            success: function (data) {
                $.each(data, function (index, element) {
                    res = "<a href='/apartments/" + data[index].id + "'><div class=\"\">\n" +
                        "            <h3 class=\"new-list-h3\">New Listings</h3>\n" +
                        "            <div class='new-img-holding' >\n" +
                        "                <img alt='new aprtment image' class=\"new-list-img\" src=\" " + data[index].image + "\" />\n" +
                        " <div class='new_img_caption'><br>" + data[index].locationID_streetname + " " + data[index].locationID_houseNum + "  " +
                        "</div> " +
                        "            </div>\n" +
                        "        </div> </a>";
                });

                $('#get_newest_apartment_app').append(res);

            }
        })
    }


    getThreeRandomApartments();
    getNewestApartment();

});