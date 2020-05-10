from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from goods.filters import GoodsFilter
from goods.models import Goods, GoodsCategory
from goods.serializers import GoodsSerializer, GoodsCategorySerializer


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 10000

class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    """
    list:
        商品列表页,搜索,分页,过滤,排序
    """
    # def get(self, request, format=None):
    #     goods = Goods.objects.all()[:10]
    #     goods_serializer = GoodsSerializer(goods, many=True)
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filterset_class =GoodsFilter
    search_fields = ['name', 'goods_brief','goods_desc']
    ordering_fields = ['sold_num', 'shop_price']



class GoodsCategoryViewSet(mixins.ListModelMixin,mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializer
