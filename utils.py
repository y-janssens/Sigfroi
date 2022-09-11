import json
from django.core.serializers.json import DjangoJSONEncoder

def toJs(data, value):
    query = data.objects.all().values(value)
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result

def stuffToJs(first, second, value):
    query_first = first.objects.all().values(value)
    query_second = second.objects.all().values(value)
    query = query_first.union(query_second)
    result = json.dumps(list(query), cls=DjangoJSONEncoder)
    return result