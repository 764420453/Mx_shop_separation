from rest_framework import serializers

from goods.models import Goods, GoodsCategory



# 三级商品分类
class GoodsCategorySerializerthree(serializers.ModelSerializer):
    class Meta:
        model=GoodsCategory
        fields='__all__'

# 二级商品分类
class GoodsCategorySerializertwo(serializers.ModelSerializer):
    sub_cat=GoodsCategorySerializerthree(many=True)
    class Meta:
        model=GoodsCategory
        fields='__all__'

# 一级商品分类
class GoodsCategorySerializer(serializers.ModelSerializer):
    sub_cat=GoodsCategorySerializertwo(many=True)
    class Meta:
        model=GoodsCategory
        fields='__all__'

# 商品序列化
class GoodsSerializer(serializers.ModelSerializer):
    category=GoodsCategorySerializer()
    class Meta:
        model=Goods
        fields="__all__"
