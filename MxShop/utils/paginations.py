from rest_framework.pagination import PageNumberPagination


class GoodsPagination(PageNumberPagination):
    def set_page(self):
        page_size = 10
        page_size_query_param = 'page_size'
        page_query_param = 'page'
        max_page_size = 10000
        return self.set_page()