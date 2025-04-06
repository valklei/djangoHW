from django.http import HttpResponse

def greetings(request):
    name = "Valerii"
    return HttpResponse(f'<h1>Hello, {name}!</h1>')
# Create your views here.
