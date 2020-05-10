from rest_framework.routers import DefaultRouter
from goods.views import GoodsListViewSet, GoodsCategoryViewSet

urlpatterns = [

]
router = DefaultRouter()
router.register('goods', GoodsListViewSet, basename='goods_list')
router.register('categorys',GoodsCategoryViewSet,basename='goods_categorys'),




urlpatterns += router.urls
