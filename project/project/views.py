# from django.http import HttpResponse,

# def index(request):
#     return HttpResponse("welcome to landing 1 page")


from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("<h5>welcome to my landing page</h5>")
    

def index(request):
    return HttpResponse("welcome to my landing page")