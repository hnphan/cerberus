$(function(){
   // notification sidebar
   $("#notifs").click(function (e) {
      e.preventDefault();
      $('#charms').charms('showSection', 'theme-charms-section');
      $.getJSON("../../system/recent_notifs/", function(data){      
         var notifHtml = "";
         if (data.length ==0) {
            notifHtml = "You have no notifications.";
         }
         else {
            for (var i=data.length-1; i>=0; i--) {
               if (data[i].seen == true) {
                  notifHtml += '<tr class = "seenNotif"><td>' + data[i].content;
               }
               else {
                  notifHtml += '<tr class = "unseenNotif"><td>' + data[i].content;
                  $.getJSON("../../system/mark_as_seen", {messageID : data[i].id},
                     function(data){});
               }
               notifHtml += '<br/><small>' + data[i].timestamp + '</small></td></tr>'
            }
         }
      $("#notifContent").html(notifHtml);
      }); 
   });

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