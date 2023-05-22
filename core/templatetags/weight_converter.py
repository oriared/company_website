from django import template

register = template.Library()

@register.filter
def convert_weight(weight):
    if weight % 1000 == 0:
        return f'{weight // 1000} кг'
    elif weight > 1000:
        return f'{weight / 1000} кг'
    else:
        return f'{weight} г'
