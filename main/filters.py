from django_filters import FilterSet, NumberFilter
from .models import Complex


class ComplexFilterOne(FilterSet):
    min_price = NumberFilter(field_name='price', lookup_expr='gte')
    max_price = NumberFilter(field_name='price', lookup_expr='lte')
    square__gte = NumberFilter(field_name='square', lookup_expr='gte')
    square__lte = NumberFilter(field_name='square', lookup_expr='lte')

    class Meta:
        model = Complex
        fields = ['district', 'num_rooms', 'min_price', 'max_price', 'square__gte', 'square__lte']


class ComplexFilterTwo(FilterSet):
    min_price = NumberFilter(field_name="price", lookup_expr='gte')
    max_price = NumberFilter(field_name="price", lookup_expr='lte')
    square__gte = NumberFilter(field_name='square', lookup_expr='gte')
    square__lte = NumberFilter(field_name='square', lookup_expr='lte')

    class Meta:
        model = Complex
        fields = ['company', 'type_of_house', 'square__gte', 'square__lte', 'min_price', 'max_price']
