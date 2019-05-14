

function getThreeRandomApartments() {
    var res = "";
    $.ajax({
                url: 'get_three_random_apartments/',
                datatype: 'json',
                type: 'GET',
                success: function(data) {
                    $.each(data, function (index, element) {
                        res += "<div class=\"carousel-item \">\n" +
                            "<a href='/apartments/" + data[index].id +"'>" +
                            "                <img width='400' height='600' src=\" " + data[index].first_image + " \" class=\"d-block w-100\" alt=\"...\">\n" +
                            "                <div class=\"carousel-caption d-none d-md-block\">\n" +
                            "              <h5 style='background-color: rgba(0,0,0,0.5)'>" + data[index].locationID_streetname + " " + data[index].locationID_houseNum + "</h5>\n" +
                            "              <p style='background-color: rgba(0,0,0,0.5)  '>" + data[index].description + "</p>\n" +
                            "                </div>\n" +
                            "                </div>\n" +
                            "</a>" +
                            "                \n";
                    });

                    $('#get_three_elements_app').append(res);

            }
    })
};

function getNewestApartment() {
    var res = "";
    $.ajax({
                url: 'get_newest_apartment/',
                datatype: 'json',
                type: 'GET',
                success: function(data) {
                    $.each(data, function (index, element) {
                        res = "<a href='/apartments/" + data[index].id + "'><div class=\"\">\n" +
                            "            <h3 class=\"new-list-h3\">New Listings</h3>\n" +
                            "            <div >\n" +
                            "                <img class=\"new-list-img\" src=\" " + data[index].image +  "\" />\n" +
                            "            </div>\n" +
                            "        </div> </a>";
                    });

                    $('#get_newest_apartment_app').append(res);

            }
    })
};


