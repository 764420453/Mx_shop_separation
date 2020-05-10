from django.db.models import Q
from rest_framework import generics
from django_filters import rest_framework as filters

from goods.models import Goods


class GoodsFilter(filters.FilterSet):
    pricemin = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    top_category=filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category=value)|Q(category__parent_category=value)|Q(category__parent_category__parent_category=value))


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax','top_category']
