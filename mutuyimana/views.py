from django.shortcuts import render


def handler_404(request):
	response = render(request,'error.html')
	response.status_code = 404
	return response

def handler_500(request):
	response = render(request,'error.html')
	response.status_code = 500
	return response

def error(request):
	return render(request, 'error.html')