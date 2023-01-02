from datetime import date
import json
from django.core.serializers.json import DjangoJSONEncoder


def toJs(data, value):
    query = data.objects.all().values(value)
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result


def chars_to_js(data, id, name, value):
    query = data.objects.filter(is_active=True).values(id, name, value).order_by('name')
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result


def list_to_js(data, id, name, inscription_date, completion_date):
    query = data.objects.all().values(id, name, inscription_date, completion_date).order_by('created')
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result


def bars_to_js(data, uuid, name, color, progress, total, symbol):
    query = data.objects.all().values(uuid, name, color, progress, total, symbol).order_by('created')
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result


def stuffToJs(first, second, value):
    query_first = first.objects.all().values(value)
    query_second = second.objects.all().values(value)
    query = query_first.union(query_second)
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result


def date_range():
    current_date = date.today()
    actual_month = current_date.replace(day=1)
    previous_month = current_date.replace(day=1, month=current_date.month - 1)
    return str(previous_month), str(actual_month)


def fill_confirmation_dict(label, action, item, ref=None):
    """
    Takes 3 arguments:
    - A label to display in confirmation modal
    - An action which is the url pattern name for the deletion view
    - And an item which is the item pk
    """
    return {'page_title': "Confirmation", 'label': label, 'action': action, 'item': item, 'ref': ref}
