import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Article


def test_view(request):
    return HttpResponse("Hello, World!")

def test_view_2(request):
    return HttpResponse("Hello, World! 2")

def test_view_3(request):
    name = request.GET.get("name")
    if name:
        return HttpResponse(f"Hello, {name}!")
    return HttpResponse("Hello, World! 3")


def article_list(request):
    articles = list(
        Article.objects.filter(published=True).values("id", "title", "created_at")
    )
    return JsonResponse({"articles": articles})


@require_http_methods(["POST"])
def article_create(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    title = data.get("title", "").strip()
    body = data.get("body", "").strip()
    if not title or not body:
        return JsonResponse({"error": "title and body are required"}, status=400)

    article = Article.objects.create(title=title, body=body)
    return JsonResponse({"id": article.id, "title": article.title}, status=201)
