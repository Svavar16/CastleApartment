
  window.onload = function () {
    $.ajax({
                url: 'get_three_random_apartments/',
                datatype: 'json',
                type: 'GET',
                success: function(data) {
                    $.each(data, function(index, element) {
                        res = "<div class=\"bd-example\">\n" +
                            "            <div id=\"carouselExampleCaptions\" class=\"carousel slide\" data-ride=\"carousel\">\n" +
                            "            <ol class=\"carousel-indicators\">\n" +
                            "            <li data-target=\"#carouselExampleCaptions\" data-slide-to=\"0\" class=\"active\"></li>\n" +
                            "            <li data-target=\"#carouselExampleCaptions\" data-slide-to=\"1\"></li>\n" +
                            "            <li data-target=\"#carouselExampleCaptions\" data-slide-to=\"2\"></li>\n" +
                            "            </ol>\n" +
                            "            <div class=\"carousel-inner\">\n" +
                            "                <div class=\"carousel-item active\">\n" +
                            "                <img src=\"https://pmcvariety.files.wordpress.com/2018/07/bradybunchhouse_sc11.jpg?w=1000&h=563&crop=1\" class=\"d-block w-100\" alt=\"...\">\n" +
                            "                <div class=\"carousel-caption d-none d-md-block\">\n" +
                            "              <h5>" + data[index].id + "</h5>\n" +
                            "              <p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>\n" +
                            "                </div>\n" +
                            "                </div>\n" +
                            "        <div class=\"carousel-item\">\n" +
                            "            <img src=\"https://pmcvariety.files.wordpress.com/2018/07/bradybunchhouse_sc11.jpg?w=1000&h=563&crop=1\" class=\"d-block w-100\" alt=\"...\">\n" +
                            "            <div class=\"carousel-caption d-none d-md-block\">\n" +
                            "              <h5>Second slide label</h5>\n" +
                            "              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>\n" +
                            "            </div>\n" +
                            "        </div>\n" +
                            "        <div class=\"carousel-item\">\n" +
                            "            <img src=\"https://pmcvariety.files.wordpress.com/2018/07/bradybunchhouse_sc11.jpg?w=1000&h=563&crop=1\" class=\"d-block w-100\" alt=\"...\">\n" +
                            "            <div class=\"carousel-caption d-none d-md-block\">\n" +
                            "            <h5>Third slide label</h5>\n" +
                            "            <p>Praesent commodo cursus magna, vel scelerisque nisl consectetur.</p>\n" +
                            "            </div>\n" +
                            "        </div>\n" +
                            "    </div>\n" +
                            "    <a class=\"carousel-control-prev\" href=\"#carouselExampleCaptions\" role=\"button\" data-slide=\"prev\">\n" +
                            "      <span class=\"carousel-control-prev-icon\" aria-hidden=\"true\"></span>\n" +
                            "      <span class=\"sr-only\">Previous</span>\n" +
                            "    </a>\n" +
                            "    <a class=\"carousel-control-next\" href=\"#carouselExampleCaptions\" role=\"button\" data-slide=\"next\">\n" +
                            "      <span class=\"carousel-control-next-icon\" aria-hidden=\"true\"></span>\n" +
                            "      <span class=\"sr-only\">Next</span>\n" +
                            "    </a>\n" +
                            "  </div>\n" +
                            "</div>"


                        $('#get_three_elements_app').append(res);
                    });
                }
            });
  };

