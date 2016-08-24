from django.conf.urls import url
from .views import articles_list, articles_list_all

urlpatterns = [
        url(r'^list/(?P<block_id>\d+)',articles_list),
        url(r'^lists$',articles_list_all),
        ]
