from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, World. You are now at the polls index.")
