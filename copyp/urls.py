from django.conf.urls import url
 
from . import views
 
urlpatterns = [
    url("user_detail", views.user_detail),
    url("user_illusts", views.user_illusts),
    url("illust_detail", views.illust_detail),
    url("illust_related", views.illust_related),
    url("illust_related_parse_qs", views.illust_related_parse_qs),
    url("illust_recommended", views.illust_recommended),
    url("illust_ranking", views.illust_ranking),
    url("search_illust", views.search_illust),
    url("ranking_all", views.ranking_all),
    url("image_download", views.image_download),
]