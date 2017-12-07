$(function() {
  $('.team').slick({
    centerMode: true,
    dots: true,
    autoplay: true,
    autoplaySpeed: 2000,
    centerPadding: '67px',
    slidesToShow: 3,
    responsive: [{
      breakpoint: 768,
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: '45px',
        slidesToShow: 2
      }
    }, {
      breakpoint: 480,
      settings: {
        arrows: true,
        centerMode: true,
        centerPadding: '45px',
        slidesToShow: 1
      }
    }]
  });




  // PORTFOLIO CAROUSEL



  
});
 // Slick Carousel
