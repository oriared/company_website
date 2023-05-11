from decimal import Decimal
from django.conf import settings
from core.models import ProductPackaging


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        product_vendor_code = product.vendor_code
        if product_vendor_code not in self.cart:
            self.cart[product_vendor_code] = {'quantity': 0}
        if override_quantity:
            self.cart[product_vendor_code]['quantity'] = quantity
        else:
            self.cart[product_vendor_code]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_vendor_code = product.vendor_code
        if product_vendor_code in self.cart:
            del self.cart[product_vendor_code]
            self.save()

    def __iter__(self):
        product_vendor_codes = self.cart.keys()
        products = ProductPackaging.objects.filter(vendor_code__in=product_vendor_codes)
        cart = self.cart.copy()
        for product in products:
            cart[product.vendor_code]['product'] = product
        for item in cart.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
