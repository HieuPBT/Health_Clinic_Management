from rest_framework.pagination import PageNumberPagination

"""
set number of results per page
"""


class UserPagination(PageNumberPagination):
    page_size = 3