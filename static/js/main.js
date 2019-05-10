$(document).ready(function () {
   $('#Test-Btn').on('click', function (e) {
      e.preventDefault();
      console.log("This should work")
      $.ajax({
           url: 'all_listing?arrange_by_price',
           type: 'GET',
           success: function (resp) {
               //var Array = resp.data.map();
               //var sortedArray  =  Array.sort(function(a, b){return a - b});
               var newHTML = resp.data.map(d => {
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
               $('#apartment-card-details').html(newHTML.join(''))
           },
           error: function (xhr, status, error) {
               // todo, a way to display the error, maybe a toastr
               console.error(error)
           }
       })
   })
});