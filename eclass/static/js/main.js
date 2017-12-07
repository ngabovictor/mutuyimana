$(document).ready(function(){
	

	$('.body').hide();
	$('.course-notes').hide();
	$('.for-multiple').hide();

	$('.side-menu-button').click(function(){
		$('.side-bar').animate({'margin-left': '0px'}, "fast");
		$('.body').show();
		$('.body').css("background-color", "rgba(0,0,0,0.5)");
	});

	$('.close').click(function(){
		$('.side-bar').animate({'margin-left': '-300px'}, "fast");
		$('.body').hide();
		$('.body').css("background-color", "transparent");
	});

	$('.body').click(function(){
		$(this).hide();
		$('.side-bar').animate({'margin-left': '-300px'}, "fast");
		$(this).css("background-color", "transparent");
	});

	// VIEW NOTES

	$('.view-note').click(function(){
		if ($(this).hasClass('show') === true) {
			$(this).removeClass('show');
			$(this).html('Hide Notes');
			$(this).addClass('hide');
			$('.course-notes').slideDown();
		}

		else if ($(this).hasClass('hide') === true) {
			$(this).removeClass('hide');
			$(this).html('View Notes');
			$(this).addClass('show');
			$('.course-notes').slideUp();
		};
	});



	// Setting an assignment

	// For multiple choice questions

		//Set to type text initially
		$('#q-type').val("text");

	$('#q-type').change(function(){
		var type = $(this).val();
		if (type == "checkbox" || type == "radio") {
			$('.all-choices').html("<div class=\"to-append\"></div>");
			$('#number-choices').val(0);
			$('.for-multiple').show();
		}

		else{
			$('.all-choices').html("<div class=\"to-append\"></div>");
			$('#number-choices').val(0);
			$('.for-multiple').hide();
		}
	});


	$('#number-choices').keyup(function(){
		var nbr = $(this).val();
		$('.all-choices').html("<div class=\"to-append\"></div>");
		for (var i = 1; i <= nbr; i++) {
			$('.to-append').append("<div class=\"form-control\"><label for=\"option" + i +"\"> Choice " + i + ":</label><input type=\"text\" id=\"option" + i +"\" name=\"option" + i +"\"></div>");
		};
	})
})