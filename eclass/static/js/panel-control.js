$(document).on('click', '.card-header a.clickable', function(e)
{
	var header = $('.clickable'),
		body = $('#card-block');
	if(body.hasClass('.show') === true)
	{
		header.find('i').removeClass('fa-plus').addClass('fa-minus');
	}

	else
	{
		header.find('i').removeClass('fa-minus').addClass('fa-plus');
	}
})