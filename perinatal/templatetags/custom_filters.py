from django import template

register = template.Library()


@register.filter(name="remove")
def remove(value, key):
    params = value.split('&')
    filtered_params = [param for param in params if not param.startswith(key + '=')]
    result = '&'.join(filtered_params)

    if result and result[-1] == '&':
        result = result[:-1]

    if result and result[0] == '&':
        result = result[1:]

    return result


@register.filter(name='get_item')
def get_item(item_list, index):
    try:
        return item_list[index]
    except (IndexError, TypeError):
        return None
