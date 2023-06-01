from django.contrib import admin

from core.models import (Product, ProductType, Category,
                         ProductDetail, ProductPack, Carousel)


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    fields = ('description', 'conditions', ('storage_time', 'storage_time_units'),
              'calories', ('proteins', 'fats', 'carbohydrates'))
    radio_fields = {'storage_time_units': admin.VERTICAL}


class ProductPackInline(admin.StackedInline):
    model = ProductPack
    fields = (('sku', 'weight', 'items_in_box', 'price'),)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_category', 'type', 'is_published')
    list_display_links = ('name',)
    fields = ('name', 'slug', 'type', 'image', ('is_gost', 'is_published'))
    search_fields = ('name',)
    list_filter = ('is_published', 'type__category')
    prepopulated_fields = {'slug': ('name',)}
    inlines = (ProductDetailInline, ProductPackInline)


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_published')
    list_filter = ('is_published',)
