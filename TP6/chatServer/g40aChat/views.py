from django.http import HttpResponse

def index(request):
    return HttpResponse("Bonjour Ceci est notre première app sur Django")
