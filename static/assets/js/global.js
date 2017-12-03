// eslint-disable-next-line no-unused-vars
(function (window, document, $, undefined) {

  window.globaldict = {};
  window.globaldict.urls = {};

  $(document).ready(function () {
    $('#map').addClass('scrolloff');                // set the mouse events to none when doc is ready
    $('#overlay-map').on('mouseup',function(){          // lock it when mouse up
      $('#map').addClass('scrolloff');               //somehow the mouseup event doesn't get call...
    });
    $('#overlay-map').on('mousedown',function(){        // when mouse down, set the mouse events free
      $('#map').removeClass('scrolloff');
    });
    $('#map').mouseleave(function () {              // becuase the mouse up doesn't work...
      $('#map').addClass('scrolloff');            // set the pointer events to none when mouse leaves the map area or you can do it on some other event
    });
  });

  $(document).ready(function(){
    var my_posts = $('[rel=tooltip]');

    var size = $(window).width();
    for(var i = 0; i < my_posts.length; i++){
      var the_post = $(my_posts[i]);

      if(the_post.hasClass('invert') && size >=767 ){
        the_post.tooltip({ placement: 'left'});
        the_post.css('cursor','pointer');
      }else{
        the_post.tooltip({ placement: 'rigth'});
        the_post.css('cursor','pointer');
      }
    }
  });

  $(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
  });


  $('#registerform').submit(function () {
    $('#loading').css('display', 'inline');
  });


  // // Not in use;
  // window.check_email = function (email) {
  //   $.ajax({
  //     url: 'check_email/',
  //     data: {'email': email},
  //     type: 'GET',
  //     success : function(data) {
  //       console.log(data);
  //     }
  //   });
  // };

})(window, window.document, window.jQuery);
