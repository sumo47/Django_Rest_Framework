from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page requested !")
    friends = ["ankit ", "aman ", "suman "]
    return JsonResponse(friends, safe=False)
