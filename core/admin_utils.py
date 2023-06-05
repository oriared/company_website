import csv

from core.models import ProductPack, PriceImport
from typing import Optional


def check_file(form_object: PriceImport) -> list[Optional[str]]:

    with form_object.csv_file.open('r') as csv_file:
        rows = csv.DictReader(csv_file)

        if sorted(rows.fieldnames) != ['price', 'sku']:
            raise ValueError('Недопустимые имена столбцов')

        no_matched = []

        for row in rows:
            price_validation(row['price'])
            if not ProductPack.objects.filter(sku=row['sku']).exists():
                no_matched.append(row['sku'])
    return no_matched


def update_prices_from_file(form_object: PriceImport, change_visability: bool) -> None:

    with form_object.csv_file.open('r') as csv_file:
        rows = csv.DictReader(csv_file)

        if change_visability:

            ProductPack.published.update(is_published=False)

            for row in rows:
                price = row['price'].replace(',', '.')

                ProductPack.objects.filter(sku=row['sku'])\
                    .update(price=price, is_published=True)

        else:
            for row in rows:
                price = row['price'].replace(',', '.')

                ProductPack.objects.filter(sku=row['sku']).update(price=price)


def price_validation(price):
    p = price.replace(',', '.')
    try:
        float(p)
    except ValueError as e:
        raise ValueError(f'Недопустимое значение цены "{p}": {e}')
