def path_category_image(instance, filename):
    return f'images/categories/{instance.slug}'


def path_product_image(instance, filename):
    return f'images/products/{instance.slug}'
