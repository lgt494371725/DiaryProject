from django.db import models
from django.utils import timezone  # djangoでは、datetime.now のかわりに、timezone.now で現在日付・時刻を取得する


class Day(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
    image = models.ImageField('画像', upload_to='images', blank=True, null=True)


    @classmethod
    def search(cls, year=None, month=None, day=None, query=None):
        qs = cls.objects.all()
        if year:
            qs = qs.filter(date__year=year)
        if month:
            qs = qs.filter(date__month=month)
        if day:
            qs = qs.filter(date__day=day)
        if query:
            query = query.strip().replace('\u200b', '').replace('\u200c', '')
            qs = qs.filter(models.Q(title__icontains=query) | models.Q(text__icontains=query))
        return qs
