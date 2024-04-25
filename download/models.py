from django.db import models

# Create your models here.


class Music(models.Model):
    class Meta:
        db_table = 'music_info'  # 表名

    id = models.AutoField(db_column='id', primary_key=True)
    name = models.CharField(max_length=1000, db_column='name', blank=False)
    artist = models.CharField(max_length=1000, db_column='artist', blank=False)
    duration = models.CharField(max_length=1000, db_column='duration', blank=True)
    album = models.CharField(max_length=1000, db_column='album', blank=False)
    released_data = models.CharField(max_length=1000, db_column='released_data', blank=False)
    pic = models.CharField(max_length=1000, db_column='pic', blank=False)
    url = models.CharField(max_length=1000, db_column='url', blank=True)


class AccessLogSearch(models.Model):
    class Meta:
        db_table = 'search_access_log'

    access_time = models.DateTimeField(db_column='search_time', auto_now=True)
    music_name = models.CharField(db_column='music_name', max_length=255)
    from_db = models.CharField(db_column='from_db', max_length=255)
    user_ip = models.CharField(db_column='user_ip', max_length=255)



