from django import template
from App.models import *

register = template.Library()


@register.inclusion_tag('App/menu.html', takes_context=True)
def draw_menu(context: dict, menu) -> dict:
    """
    Построение древовидного меню
    """
    try:
        filter_item_id = int(context['request'].GET[menu])
        items = Menu.objects.filter(category__name=menu)
        items_values = items.values()
        main_item = [item for item in items_values.filter(parent=None)]
        filter_items_id_list = filter_item_id_list(
            items.get(id=filter_item_id),
            main_item,
            filter_item_id
        )

        for item in main_item:
            if item['id'] in filter_items_id_list:
                item['childs'] = child(
                    items_values, item['id'], filter_items_id_list
                )
        item_dict = {'items': main_item}

    except:
        item_dict = {
            'items': [
                item
                for item in Menu.objects.filter(
                    category__name=menu, parent=None
                ).values()
            ]
        }

    item_dict['menu'] = menu
    item_dict['additional_menu'] = additional_menu(context, menu, [])
    return {'items': item_dict['items'], 'menu': menu, 'additional_menu':additional_menu}


def filter_item_id_list(parent, main_item: list, filter_item_id: list) -> list:
    """
    Метод вовзращает список id "родителей"
    """
    items_id = []
    while parent:
        items_id.append(parent.id)
        parent = parent.parent
    else:
        for item in main_item:
            if item['id'] == filter_item_id:
                items_id.append(filter_item_id)
    return items_id


def child(items_values, cur_id: int, filter_item_id_list: list) -> list:
    """
    Метод возвращает список вложенных элементов в меню
    """
    lst_items = [it for it in items_values.filter(parent_id=cur_id)]
    for item in lst_items:
        if item['id'] in filter_item_id_list:
            item['childs'] = child(
                items_values, item['id'], filter_item_id_list
            )
    return lst_items


def additional_menu(context: dict, menu: str, querystring_args: list):
    """
    Получение дополнительного меню,
    для вывода нескольких меню на одной странице
    """
    for key_menu in context['request'].GET:
        if key_menu != menu:
            querystring_args.append(
                key_menu + '=' + context['request'].GET[key_menu]
            )
    return ('&').join(querystring_args)
