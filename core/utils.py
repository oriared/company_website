from django.db.models import Model


def path_category_image(instance: Model, filename: str) -> str:
    return f'images/categories/{instance.slug}'


def path_product_image(instance: Model, filename: str) -> str:
    return f'images/products/{instance.slug}'
