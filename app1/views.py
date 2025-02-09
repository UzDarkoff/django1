from django.http import HttpResponse

def hello(request):
    return HttpResponse('salom django')
def salom(request):
    return HttpResponse('hello django')
def new(request):
    return HttpResponse('new django')
