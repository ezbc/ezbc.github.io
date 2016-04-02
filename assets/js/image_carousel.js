/* Slick Carousel functional adjustments
https://kenwheeler.github.io/slick/ 
*/
$(document).ready(function(){
    $('.autoplay').slick({
      slidesToShow: 2,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
    });

    $('.variable-width').slick({
      dots: true,
      infinite: true,
      speed: 300,
      slidesToShow: 1,
      centerMode: true,
      variableWidth: true,
    });

    $('.fade').slick({
      dots: true,
      infinite: true,
      speed: 500,
      fade: true,
      cssEase: 'linear'
    });

    $('.multiple-items').slick({
      infinite: true,
      slidesToShow: 3,
      slidesToScroll: 3
    });

    $('.single-item').slick({
      centerMode: true,
      dots: true,
    });

});


