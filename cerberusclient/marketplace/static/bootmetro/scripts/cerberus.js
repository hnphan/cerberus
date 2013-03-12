$(function(){

// check for new notifications
setInterval(function() {
   $.getJSON("../../system/check_notifs/", function(data){
      if (data.count > 0) {
         icon = document.getElementById("notiIcon");
         icon.className = "icon-spinner icon-3x icon-spin";
         icon.style.color = 'red';
         icon.style.textDecoration = 'none';
      }
      else {
         icon = document.getElementById("notiIcon");
         icon.className = "icon-spinner icon-3x";
         icon.style.color = 'grey';
         icon.style.textDecoration = 'none';
      }
   }); 
}, 500);

});