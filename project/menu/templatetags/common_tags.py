from django import template
from menu.models import Menu
from django.http import HttpResponse
register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def show_menu(context, name):
    request = context.get('request')
    current_url = request.path.strip('/') if request else ''

    root_item = Menu.objects.filter(name=name).first()
    menu_items = root_item.get_children() if root_item else []
    return {
        "menu_items": menu_items,
        "current_url": current_url,
    }