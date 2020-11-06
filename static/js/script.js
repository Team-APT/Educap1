$(".wish_button" ).click(function() {
    var x = $(this).text();
    if (x == "Add to Wishlist")
   {
        $(this).addClass('selected').removeClass('unselected');
        $(this).text("Wishlisted")
   }
    else
  {  
        $(this).addClass('unselected').removeClass('selected');
        $(this).text("Add to Wishlist")
  }

});


 