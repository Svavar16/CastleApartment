
  window.onload = function () {
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
  })};

