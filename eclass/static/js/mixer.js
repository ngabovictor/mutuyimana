$(document).ready(function(){
	$(function(){
	  var $container = $('#projects'),
	      $controls = $('.controls');
	  
	  $container.mixItUp({
	    animation: {
	      duration: 700,
	      effects: 'fade translateY(600%) stagger(35ms)',
	      easing: 'cubic-bezier(0.86, 0, 0.07, 1)',
	      reverseOut: true
	    },
	    controls: {
	      enable: false
	    }
	  });
	  
	  $controls.on('click', '.filter', function(){
	    var $btn = $(this),
	        filter = $btn.attr('data-filter');

	    $container.mixItUp('filter', 'none', function(){
	      $container.mixItUp('filter', filter);
	    });
	  });
	  
	});
})