from django.contrib import admin

from .models import Product, ProductType, Category, ProductDetail, Carousel


class ProductDetailAdmin(admin.StackedInline):
    model = ProductDetail
    fields = ('vendor_code', 'description', 'conditions', 'packaging',
              'calories', ('proteins', 'fats', 'carbohydrates'))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'weight', 'is_published')
    list_display_links = ('name', 'type')
    search_fields = ('name',)
    list_filter = ('is_published',)
    prepopulated_fields = {'slug': ('name', 'weight')}
    inlines = [ProductDetailAdmin]


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_active')
    list_filter = ('is_active',)
