from django.http import HttpResponse

from pixivpy3 import *

import json


def pixivAuthApi():
    # api = AppPixivAPI()

    api = ByPassSniApi()
    api.require_appapi_hosts(hostname="public-api.secure.pixiv.net")
    api.set_accept_language('zh-cn')

    api.login("lishalom@sina.com", "p6569653")
    return api

def pixivApi():
    # api = AppPixivAPI()

    api = ByPassSniApi()
    api.require_appapi_hosts(hostname="public-api.secure.pixiv.net")
    api.set_accept_language('zh-cn')
    return api

# 获取作者详情
def user_detail(request):
    api = pixivAuthApi()
    json_result = api.user_detail(request.GET.get('user_id'))
    return HttpResponse(json.dumps(json_result))


# 用户作品列表 
def user_illusts(request):
    api = pixivAuthApi()
    json_result = api.user_illusts(request.GET.get('user_id'))
    return HttpResponse(json.dumps(json_result))


# 作品详情 (无需登录，同PAPI.works)
def illust_detail(request):
    api = pixivAuthApi()
    json_result = api.illust_detail(request.GET.get('illust_id'))
    return HttpResponse(json.dumps(json_result))


# 相关作品列表
def illust_related(request):
    api = pixivAuthApi()
    json_result = api.illust_related(request.GET.get('illust_id'))
    return HttpResponse(json.dumps(json_result))


# 作品相关推荐-下一页 (.parse_qs(next_url) 用法)
def illust_related_parse_qs(request):
    api = pixivAuthApi()
    next_qs = api.parse_qs(request.GET.get('next_url'))
    json_result = api.illust_related(**next_qs)
    return HttpResponse(json.dumps(json_result))


# 插画推荐 (Home - Main) 
# content_type: [illust, manga]
def illust_recommended(request):
    api = pixivAuthApi()
    json_result = api.illust_recommended()
    return HttpResponse(json.dumps(json_result))


# xxxx-xx-xx的过去一周排行
def illust_ranking(request):
    api = pixivAuthApi()
    json_result = api.illust_ranking('week', date=request.GET.get('date'))
    return HttpResponse(json.dumps(json_result))


# 按标签搜索作品
def search_illust(request):
    api = pixivAuthApi()
    json_result = api.search_illust(request.GET.get('keyword'))
    return HttpResponse(json.dumps(json_result))


# 排行榜/过去排行榜
# mode:
#   daily - 每日
#   weekly - 每周
#   monthly - 每月
#   male - 男性热门
#   female - 女性热门
#   original - 原创
#   rookie - Rookie
#   daily_r18 - R18每日
#   weekly_r18 - R18每周
#   male_r18
#   female_r18
#   r18g
def ranking_all(request):
    api = pixivAuthApi()
    json_result = api.ranking_all(request.GET.get('mode'), 1, 50)
    return HttpResponse(json.dumps(json_result))