from django_filters.rest_framework import DjangoFilterBackend as filters


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filter.FilterSet):
    products = CharFilterInFilter(field_name='products__product', lookup_expr='in' )