import csv

from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path, reverse

from core.forms import PriceImportForm
from core.models import (Product, ProductType, Category, ProductDetail,
                         ProductPack, PriceImport, Carousel)

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


@admin.register(PriceImport)
class PriceImportAdmin(admin.ModelAdmin):
    list_display = ('csv_file', 'date_added')

    def get_urls(self):
        urls = super().get_urls()
        urls.insert(-1, path('csv-upload/', self.upload_csv))
        return urls

    def upload_csv(self, request):
        if request.method == 'POST':
            form = PriceImportForm(request.POST, request.FILES)
            if form.is_valid():
                form_object = form.save()
                try:
                    update_prices_from_file(form_object)
                    messages.success(request, 'Файл успешно импортирован')
                    return redirect(reverse('admin:index'))
                except ValueError as e:
                    messages.warning(request, e)

        form = PriceImportForm()
        return render(request, 'admin/csv_import_page.html', {'form': form})


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('description', 'is_published')
    list_filter = ('is_published',)


def update_prices_from_file(form_object):
    with form_object.csv_file.open('r') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        if next(rows) != ['sku', 'price']:
            raise ValueError('Неправильные имена столбцов')
        for row in rows:
            ProductPack.objects.filter(sku=row[0]).update(price=row[1])