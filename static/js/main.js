$(document).ready(function () {

    // Search for an apartment from address
    $('#search-text-Btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: 'all_listing?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                if (!$.trim(resp.data)) {
                    $('#apartment-card-details').html('<div class="new-list-h3 sell-house house-listing"><h2>unable to find any listings at the searched address</h2></div>')
                    $('#search-box').val('');
                }
                else {
                    var newHTML = resp.data.map(d => {
                        return `<div class="col-lg-4 house-listing">
                                <div class="card">
                                    <img src="${d.firstImage}" class="card-img-top card-img-size" alt="Apartment Image">
                                    <div class="card-body">
                                        <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                        <p class="card-text">${d.description}</p>
                                    </div>
                                    <ul class="list-group list-group-flush">
                                        <li class="list-group-item">Price: ${d.price} Kr</li>
                                        <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                        <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                    </ul>
                                    <div class="card-body">
                                        <a href="${d.id}" class="card-link">More Details</a>
                                    </div>
                                </div>
                               </div>`
                    });
                    $('#apartment-card-details').html(newHTML.join(''));
                    $('#search-box').val('');
                }
            },
            error: function (xhr, status, error) {
                console.error(error)
            }
        })
    });

    // Arrange apartments by price, should return the most expensive first
    $('#sort-by-price-asc').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: 'all_listing?arrange_by_price',
            type: 'GET',
            success: function (resp) {
                //var Array = resp.data.map();
                //var sortedArray  =  Array.sort(function(a, b){return a - b});
                var newHTML = resp.data.map(d => {
                    return `<div class="col-lg-4 house-listing" >
                            <div class="card">
                                <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                <div class="card-body">
                                    <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                    <p class="card-text">${d.description}</p>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Price: ${d.price} Kr</li>
                                    <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                    <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                </ul>
                                <div class="card-body">
                                    <a href="${d.id}" class="card-link">More Details</a>
                                </div>
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
            },
            error: function (xhr, status, error) {
                // todo, a way to display the error, maybe a toastr
                console.error(error)
            }
        })
    });

    // Arrange apartments by price, should return the least expensive first
    $('#sort-by-price-desc').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: 'all_listing?arrange_by_price',
            type: 'GET',
            success: function (resp) {
                //var Array = resp.data.map();
                //var sortedArray  =  Array.sort(function(a, b){return a - b});
                var newHTML = resp.data.map(d => {
                    return `<div class="col-lg-4 house-listing" >
                            <div class="card">
                                <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                <div class="card-body">
                                    <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                    <p class="card-text">${d.description}</p>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Price: ${d.price} Kr</li>
                                    <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                    <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                </ul>
                                <div class="card-body">
                                    <a href="${d.id}" class="card-link">More Details</a>
                                </div>
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
            },
            error: function (xhr, status, error) {
                // todo, a way to display the error, maybe a toastr
                console.error(error)
            }
        })
    });

    // sort by name ascending
    $('#sort-name-asc').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: 'all_listing?sort_name_asc',
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    return `<div class="col-lg-4 house-listing" >
                            <div class="card">
                                <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                <div class="card-body">
                                    <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                    <p class="card-text">${d.description}</p>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Price: ${d.price} Kr</li>
                                    <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                    <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                </ul>
                                <div class="card-body">
                                    <a href="${d.id}" class="card-link">More Details</a>
                                </div>
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error)
            }
        })
    });

    // sort by name descending
    $('#sort-name-desc').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: 'all_listing?sort_name_desc',
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    return `<div class="col-lg-4 house-listing" >
                            <div class="card">
                                <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                <div class="card-body">
                                    <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                    <p class="card-text">${d.description}</p>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Price: ${d.price} Kr</li>
                                    <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                    <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                </ul>
                                <div class="card-body">
                                    <a href="${d.id}" class="card-link">More Details</a>
                                </div>
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
            },
            error: function (xhr, status, error) {
                console.error(error)
            }
        })
    });

    //search by postal code
    $('#search-Btn-postal').on('click', function (e) {
        e.preventDefault();
        var postal_text = $('#search-box-postal').val();
        console.log(postal_text);
        $.ajax({
            url: 'all_listing?search_postal=' + postal_text,
            type: 'GET',
            success: function (resp) {
                if (!$.trim(resp.data)) {
                    $('#Index-bottom-row-search-function').html('<div class="new-list-h3 sell-house house-listing"><h2>unable to find any listings at the searched post code</h2></div>')
                    $('#search-box-postal').val('');
                }
                else {
                    var newHTML = resp.data.map(d => {
                        return `<div class="col-lg-4 house-listing">
                                    <div class="card">
                                        <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                        <div class="card-body">
                                            <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                            <p class="card-text">${d.description}</p>
                                        </div>
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item">Price: ${d.price} Kr</li>
                                            <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                            <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                        </ul>
                                        <div class="card-body">
                                            <a href="${d.id}" class="card-link">More Details</a>
                                        </div>
                                    </div>
                                   </div>`
                    });
                    $('#Index-bottom-row-search-function').html(newHTML.join(''));
                    $('#search-box-postal').val('');
                }
            },
            error: function (xhr, status, error) {
                console.error(error)
            }
        })
    });

    //search function from the index
    $('#main-search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#main-search-text').val();
        $.ajax({
            url: '?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                if (!$.trim(resp.data)) {
                    $('#Index-bottom-row-search-function').html('<div class="new-list-h3 sell-house house-listing"><h2>unable to find any listings at the searched address</h2></div>')
                    $('#main-search-text').val('');
                }
                else {
                    var newHTML = resp.data.map(d => {
                        return `<div class="col-lg-4 house-listing">
                                    <div class="card">
                                        <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                        <div class="card-body">
                                            <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                            <p class="card-text">${d.description}</p>
                                        </div>
                                        <ul class="list-group list-group-flush">
                                            <li class="list-group-item">Price: ${d.price} Kr</li>
                                            <li class="list-group-item">Size: ${d.size} m<sup>2</sup></li>
                                            <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                        </ul>
                                        <div class="card-body">
                                            <a href="${d.id}" class="card-link">More Details</a>
                                        </div>
                                    </div>
                                   </div>`
                    });
                    $('#Index-bottom-row-search-function').html(newHTML.join(''));
                    $('#main-search-text').val('');
                }
            },
            error: function (xhr, status, error) {
                // todo, a way to display the error
                console.error(error)
            }
        })
    });

    //checks with the user if he want do back from a form or not, notifies him that he will lose his/her data
    var formhaschanged = false;
    var submitted = false;
    $(document).on('change', 'form.form-horizontal', function () {
        formhaschanged = true;
    });
    window.onbeforeunload = function (e) {
        if (formhaschanged && !submitted) {
            var message = "You have unsaved information, they might be lost", e = e || window.event;
            if (e) {
                e.returnValue = message;
            }
        }
    };
    $('form').submit(function () {
        submitted = true;
    });
});