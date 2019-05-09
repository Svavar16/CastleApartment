$(document).ready(function () {
    $('#arrange_by_price_btn').on('click', function (e){
        e.preventDefault();
        $.ajax({
            url: 'apartments/all_listing',
            type: 'GET',
            success: function (resp) {
                var Array = resp.data.map();
                var sortedArray  =  Array.sort(function(a, b){return a - b});
                console.log(sortedArray);
                var newHTML = sortedArray(d => {
                    return `<div class="card" style="width: 18rem;">
                                <a href="/apartments/${d.id}">
                                    <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                    <div class="card-body">
                                        <h5 class="card-title">${d.locationID.streetName} ${d.locationID.houseNumber} </h5>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                    </div>
                                    <ul class="list-group list-group-flush">
                                        <li class="list-group-item">Price: ${d.price}</li>
                                        <li class="list-group-item">Size: ${d.size}</li>
                                        <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                    </ul>
                                    <div class="card-body">
                                        <a href="${d.id}" class="card-link">More Details</a>
                                    </div>
                                </a>
                            </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
            },
            error: function (xhr, status, error) {
                // todo: show the error, with toaster
                console.error(error);
            }
        })
    });
});