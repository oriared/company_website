import typing


if typing.TYPE_CHECKING:
    from core.models import Category, Product


def path_category_image(instance: 'Category', filename: str) -> str:
    return f'images/categories/{instance.slug}'


def path_product_image(instance: 'Product', filename: str) -> str:
    return f'images/products/{instance.slug}'
