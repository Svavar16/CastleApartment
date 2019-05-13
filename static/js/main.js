$(document).ready(function () {
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
                return `<div class="col-lg-4" >
                            <div class="card">
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
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
                $('#search-box').val('');
         },
         error: function (xhr, status, error) {
            // todo, a way to display the error
            console.error(error)
         }
      })
   });

   // Arrange apartments by price, should return the most expensive first
   $('#sort-by-price-asc').on('click', function (e) {
      e.preventDefault();
      console.log("Arrange by price asc works!");
      $.ajax({
           url: 'all_listing?arrange_by_price',
           type: 'GET',
           success: function (resp) {
               //var Array = resp.data.map();
               //var sortedArray  =  Array.sort(function(a, b){return a - b});
               var newHTML = resp.data.map(d => {
                   return `<div class="col-lg-4" >
                            <div class="card">
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
      console.log("Arrange by price desc works!");
      $.ajax({
           url: 'all_listing?arrange_by_price',
           type: 'GET',
           success: function (resp) {
               //var Array = resp.data.map();
               //var sortedArray  =  Array.sort(function(a, b){return a - b});
               var newHTML = resp.data.map(d => {
                   return `<div class="col-lg-4" >
                            <div class="card">
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
       console.log("Sort by asc works!");
       $.ajax({
       url: 'all_listing?sort_name_asc',
       type: 'GET',
       success: function (resp) {
           var newHTML = resp.data.map(d => {
                return `<div class="col-lg-4" >
                            <div class="card">
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
       console.log("Sort by desc works!");
       $.ajax({
       url: 'all_listing?sort_name_desc',
       type: 'GET',
       success: function (resp) {
           var newHTML = resp.data.map(d => {
                return `<div class="col-lg-4" >
                            <div class="card">
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
       console.log("Postal search works!");
       var postal_text = $('#search-box-postal').val();
       console.log(postal_text);
       $.ajax({
           url: 'all_listing?search_postal=' + postal_text,
           type: 'GET',
           success: function (resp) {
               var newHTML = resp.data.map(d => {
                return `<div class="col-lg-4" >
                            <div class="card">
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
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
                $('#search-box-postal').val('');
           },
           error: function (xhr, status, error) {
               console.error(error)
           }
       })
   });

    //search function from the index
    $('#main-search-btn').on('click', function (e) {
      e.preventDefault();
      console.log("Search index Works!");
      var searchText = $('#main-search-text').val();
      window.open("/apartments/all_listing");
      $.ajax({
         url: 'all_listing?search_filter=' + searchText,
         type: 'GET',
         success: function (resp) {
            var newHTML = resp.data.map(d => {
                return `<div class="col-lg-4" >
                            <div class="card">
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
                            </div>
                           </div>`
                });
                $('#apartment-card-details').html(newHTML.join(''));
                $('#search-box').val('');
         },
         error: function (xhr, status, error) {
            // todo, a way to display the error
            console.error(error)
         }
      })
   });
});