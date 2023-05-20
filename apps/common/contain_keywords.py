import operator
from functools import reduce

from django.db.models import Q


def generate_contains_query(search_cols, search_key):
    contain_formula = {}
    for column in search_cols:
        contain_formula[column + "__contains"] = search_key
    return reduce(operator.or_, [Q(_connector=Q.OR, **contain_formula)])
