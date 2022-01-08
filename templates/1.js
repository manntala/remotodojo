var element = document.createElement('select');
element.style.width = "100px";


function displayWidget(){
  document.getElementById("Product-content-5-6944255508687-6944255508687").setAttribute("height", "0% !important");
}

(function () {
  document.getElementById(".collapsible-content__inner").setAttribute("height", 0);
   	console.log("loaded");
}());


document.getElementById("myBtn").addEventListener("click", myFunction);

function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}

$(document).ready(function() {


  var $offHeight = 0

  function updateHeight() {
    var $tempHeight = 0;
    var $wrapper = $('.collapsibles-wrapper collapsibles-wrapper--product');
    $tempHeight += $('.row').not('.mainRow').outerHeight();
    $tempHeight += $('#panel1').find('.panel-heading').outerHeight();
    $tempHeight += $('#panel2').find('.panel-heading').outerHeight() + 5 + 4; // +5 for margin-top of panel 2 header and +4 for adjustment 
    $offHeight = $wrapper.height() - $tempHeight;
    $('#collapseOne').css({

      'max-height': $offHeight
    });
    $('#collapseTwo').css({

      'max-height': $offHeight
    });



  }

  updateHeight();


  $('.panel-heading').on('click', function() {

    updateHeight();



  });

  $(window).resize(function() {


    updateHeight();

  });


});


jQuery('.yotpo-default-button.yotpo-icon-btn.pull-right.yotpo-hidden-mobile.write-button.write-review-button').on('click' , function(){jQuery('.collapsible-trigger__layout').trigger('click');});


function(){ jQuery('..yotpo-default-button .yotpo-icon-btn .pull-right .yotpo-hidden-mobile .write-button .write-review-button').on('click' , 
function(){jQuery('.label .collapsible-trigger .collapsible-trigger-btn .collapsible-trigger-btn--borders)').trigger('click');});});



    $( document ).ready(function(){
        jQuery('.yotpo-default-button.yotpo-icon-btn.pull-right.yotpo-hidden-mobile.write-button.write-review-button').on('click' ,
        function(){
            jQuery('.collapsible-trigger__layout').trigger('click');
            var element = document.getElementById("label collapsible-trigger collapsible-trigger-btn collapsible-trigger-btn--borders collapsible--auto-height");
            element.classList.add("is-open");
        });
    });


    $( document ).ready(function(){
      jQuery('#Product-content-5-6908885172431-6908885172431 > div > div.yotpo.yotpo-main-widget > div > div.yotpo-display-wrapper > div.yotpo-regular-box.yotpo-bottomline.yotpo-bottomline-2-boxes.yotpo-bottomline-empty-state > div.yotpo-default-button.yotpo-icon-btn.pull-right.yotpo-hidden-mobile.write-button.write-review-button').on('click' ,
      function(){
          console.log("working");
          document.getElementsById('#Product-content-5-6908885172431-6908885172431')[0].setAttribute("style", "height:900px !important");
          jQuery('#collapsible-trigger__layout').trigger('click');
         
          
      });
  });
  #Product-content-5-6908885172431-6908885172431 > div > div.yotpo.yotpo-main-widget > div > div.yotpo-display-wrapper > div.yotpo-regular-box.yotpo-bottomline.yotpo-bottomline-2-boxes.yotpo-bottomline-empty-state > div.yotpo-default-button.yotpo-icon-btn.pull-right.yotpo-hidden-mobile.write-button.write-review-button
  var divClicked = document.querySelector('div.page-content.page-content--product > div.page-width.page-width--flush-small > div.collapsibles-wrapper.collapsibles-wrapper--product > button').click();


  


window.onload=function(){
  var element = document.getElementsByClassName('label collapsible-trigger collapsible-trigger-btn collapsible-trigger-btn--borders collapsible--auto-height is-open')[0];
element.addEventListener("click", function(e) {
    alert('something');
}, false);
}

#

$( document ).ready(function(){
  jQuery('.yotpo-icon.yotpo-icon-write').on('click' ,
  function(){
      console.log("working");
      document.querySelector('#Product-content-5-')[0].setAttribute("style", "height:900px !important");
      jQuery('#collapsible-trigger__layout').trigger('click');
     
      
  });
});


$(document).ready(function() {
  $('label collapsible-trigger collapsible-trigger-btn collapsible-trigger-btn--borders collapsible--auto-height is-open').click(function() {
      alert('ho ho ho');
  });
});


<script>
  window.onload=function(){
  var element = document.getElementsByClassName('label collapsible-trigger collapsible-trigger-btn collapsible-trigger-btn--borders collapsible--auto-height is-open')[0];
  element.addEventListener("click", function(e) {
    document.getElementsByClassName('.collapsible-content__inner')[0].setAttribute("style", "height:0");;
}, false);
}
  
</script>  