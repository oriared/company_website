from django.conf import settings
from core.models import ProductPackaging


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_sku, quantity):
        if product_sku not in self.cart:
            self.cart[product_sku] = {'quantity': 0}
        self.cart[product_sku]['quantity'] += quantity
        self.save()

    def update(self, product_sku, quantity):
        self.cart[product_sku]['quantity'] = quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product_sku):
        if product_sku in self.cart:
            del self.cart[product_sku]
            self.save()

    def __iter__(self):
        skus = self.cart.keys()
        product_packages = ProductPackaging.objects.filter(sku__in=skus)
        cart = self.cart.copy()
        for package in product_packages:
            cart[package.sku]['packaging'] = package
            cart[package.sku]['product'] = package.product
        for item in cart.values():
            item['total_weight'] = item['packaging'].get_package_weight() * item['quantity']
            yield item

    def __len__(self):
        return len(self.cart)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
