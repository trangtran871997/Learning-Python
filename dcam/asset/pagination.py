import math
from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPageNumber(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        page_count = math.ceil(self.page.paginator.count/self.page_size)
        page_range = range(1, page_count + 1)
        return Response(OrderedDict([
             ('lastPage', page_count),
             ('countItemsOnPage', self.page_size),
             ('number', self.page.number),
             ('next', self.get_next_link()),
             ('previous', self.get_previous_link()),
             ('previous_page_number', self.page.number - 1),
             ('next_page_number', self.page.number + 1),
             ('page_range', page_range),
             ('total', self.page.paginator.count),
             ('results', data)
         ]))
