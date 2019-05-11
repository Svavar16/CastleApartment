$(document).ready(function () {
   // Arrange apartments by price, should return the most expensive first
   $('#sort-by-price-Btn').on('click', function (e) {
      e.preventDefault();
      console.log("Arrange by price works!");
      $.ajax({
           url: 'all_listing?arrange_by_price',
           type: 'GET',
           success: function (resp) {
               //var Array = resp.data.map();
               //var sortedArray  =  Array.sort(function(a, b){return a - b});
               var newHTML = resp.data.map(d => {
                   return `<div class="card" style="width: 18rem;">
                                <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                                <div class="card-body">
                                    <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                    <p class="card-text">${d.description}</p>
                                </div>
                                <ul class="list-group list-group-flush">
                                    <li class="list-group-item">Price: ${d.price}</li>
                                    <li class="list-group-item">Size: ${d.size}</li>
                                    <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                                </ul>
                                <div class="card-body">
                                    <a href="${d.id}" class="card-link">More Details</a>
                                </div>
                            </div>`
               });
               $('#apartment-card-details').html(newHTML.join(''))
           },
           error: function (xhr, status, error) {
               // todo, a way to display the error, maybe a toastr
               console.error(error)
           }
       })
   });
   // Search for an apartment from address
   $('#search-text-Btn').on('click', function (e) {
      e.preventDefault();
      console.log("Search Works!");
      var searchText = $('#search-box').val();
      $.ajax({
         url: 'all_listing?search_filter=' + searchText,
         type: 'GET',
         success: function (resp) {
            var newHTML = resp.data.map(d => {
                return `<div class="card" style="width: 18rem;">
                             <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                             <div class="card-body">
                                 <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                 <p class="card-text">${d.description}</p>
                             </div>
                             <ul class="list-group list-group-flush">
                                 <li class="list-group-item">Price: ${d.price}</li>
                                 <li class="list-group-item">Size: ${d.size}</li>
                                 <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                             </ul>
                             <div class="card-body">
                                 <a href="${d.id}" class="card-link">More Details</a>
                             </div>
                         </div>`
               });
               $('#apartment-card-details').html(newHTML.join(''))
         },
         error: function (xhr, status, error) {
            // todo, a way to display the error
            console.error(error)
         }
      })
   });
   $('#sort-name-asc').on('click', function (e) {
       e.preventDefault();
       console.log("Sort by asc works!");
       $.ajax({
       url: 'all_listing?sort_name_asc',
       type: 'GET',
       success: function (resp) {
           var newHTML = resp.data.map(d => {
                return `<div class="card" style="width: 18rem;">
                             <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                             <div class="card-body">
                                 <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                 <p class="card-text">${d.description}</p>
                             </div>
                             <ul class="list-group list-group-flush">
                                 <li class="list-group-item">Price: ${d.price}</li>
                                 <li class="list-group-item">Size: ${d.size}</li>
                                 <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                             </ul>
                             <div class="card-body">
                                 <a href="${d.id}" class="card-link">More Details</a>
                             </div>
                         </div>`
               });
               $('#apartment-card-details').html(newHTML.join(''))
           },
           error: function (xhr, status, error) {
               console.error(error)
           }
       })
   });
   $('#search-Btn-postal').on('click', function (e) {
       e.preventDefault();
       console.log("Postal search works!");
       var postal_text = $('#')
       $.ajax({
           url: 'all_listing?search_postal',
           type: 'GET',
           success: function (resp) {
               var newHTML = resp.data.map(d => {
                return `<div class="card" style="width: 18rem;">
                             <img src="${d.firstImage}" class="card-img-top" alt="Apartment Image">
                             <div class="card-body">
                                 <h5 class="card-title">${d.locationID_streetName} ${d.locationID_houseNumber}</h5>
                                 <p class="card-text">${d.description}</p>
                             </div>
                             <ul class="list-group list-group-flush">
                                 <li class="list-group-item">Price: ${d.price}</li>
                                 <li class="list-group-item">Size: ${d.size}</li>
                                 <li class="list-group-item">Year Build: ${d.yearBuild}</li>
                             </ul>
                             <div class="card-body">
                                 <a href="${d.id}" class="card-link">More Details</a>
                             </div>
                         </div>`
               });
               $('#apartment-card-details').html(newHTML.join(''))
           },
           error: function (xhr, status, error) {
               console.error(error)
           }
       })
   })
});