from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response

class MypageNumberPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            "total":self.page.paginator.count,
            "page":self.page.number,
            "size":self.get_page_size(self.request),
            "data":data
        })