from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Hello, World!")

def test_view_2(request):
    return HttpResponse("Hello, World! 2")

def test_view_3(request):
    if request.query_params.get("name"):
        return HttpResponse(f"Hello, {request.query_params.get('name')}!")
    else:
        return HttpResponse("Hello, World! 3")
