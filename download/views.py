from django.shortcuts import render, get_object_or_404
from .models import Music, AccessLogSearch
from django.db.models import Q
from utils import download_music
import random


def index(request):
    return render(request, 'music/index.html')


def detail(request, id):
    # get_object_or_404() 抛出404错误的快捷方式
    music = get_object_or_404(Music, pk=id)

    return render(request, 'music/detail.html', {'music': music})


def results(request):
    return render(request, 'music/result.html')


def search(request):
    # 获取到用户提交的搜索关键词
    search_text = request.GET['search_text']
    print("aa" + search_text)

    if not search_text:
        return render(request, 'music/index.html')
    # 多个条件查找，两种方式
    # reponse_list = Music.objects.filter(name__icontains=search_text) | Music.objects.filter(
    #     singer__icontains=search_text)
    # 首先从数据库查找是否存在歌曲，如果存在直接返回。
    reponse_list = Music.objects.filter(Q(name=search_text))
    from_db = "yes"
    # response_list的类型是：<class 'django.db.models.query.QuerySet'>
    # 如果不存在，则从网上爬取资源并入库。
    if not reponse_list:
        reponse_list = download_music.DownMusic(search_text).run()
        from_db = "no"
        if reponse_list:
            music_obj_list = []
            for i in reponse_list:
                music_obj_list.append(
                    Music(
                        name=i['name'],
                        artist=i['artist'],
                        duration=i['duration'],
                        released_data=i['released_data'],
                        album=i['name'],
                        url=i['url'],
                        pic=i['pic']
                    )
                )
            Music.objects.bulk_create(music_obj_list)
    else:
        reponse_list = list(reponse_list.values())

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    access_log = AccessLogSearch(music_name=search_text, from_db=from_db, user_ip=ip)
    access_log.save()

    # 记录搜索数据，以后可能用到
    with open('record.txt', 'a', encoding='utf-8') as fp:
        if not reponse_list:
            fp.write('\n' + search_text + '\t0')  # 数据库中没有，0
        else:
            fp.write('\n' + search_text + '\t1')  # 数据库中存在 1
    return render(request, 'music/result.html', {'reponse_list': reponse_list})


def good_luck(request):
    """随机返回6个结果,加1句毒鸡汤"""
    with open('poison-soup.txt', 'r+', encoding='utf-8') as fp:
        soup = fp.readlines()
    poison = random.choice(soup)
    luck = Music.objects.order_by('?')[:20].values()
    return render(request, 'music/result.html', {'reponse_list': list(luck)})