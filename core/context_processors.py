from django.http.request import HttpRequest

from core.models import Category


def categories(request: HttpRequest) -> dict:
    return {'categories': Category.published.all()}
