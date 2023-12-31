from django.http.response import JsonResponse
# Create your views here.
def list_1(request):
    lm={
        'name':'name'
    }
    return JsonResponse(lm)
