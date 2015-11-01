from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import JsonResponse

from sakuya.accounts.models import Child


pos_table = [
    ('n', '名詞'),
    ('v', '動詞'),
    ('adj', '形容詞'),
    ('adv', '副詞'),
    ('im', '感動詞'),
    ('j', '助詞'),
    ('conj', '接続詞'),
    ('auv', '助動詞'),
    ('p', '接頭詞'),
    ('t', '連体詞'),
    ('unk', '未知語'),
]

def query(reuest, child_id):
#    import pdb; pdb.set_trace()
    res = {}

    try:
        child = Child.objects.get(id=child_id)
    except:
        res['status'] = 'error'
        res['reason'] = 'child not found'
        return JsonResponse(res)

    words = child.word_set.all()
    birth = child.birth
   
    for pos in pos_table:
        pos_res = {}
        pos_words = words.filter(pos1=pos[1])
        pos_res['count'] = pos_words.count()
        pos_res['words'] = [word['base'] for word in pos_words.values('base')]
        pos_res['monthly'] = get_words_monthly(pos_words, birth, range(0, 16))
        res[pos[0]] = pos_res
        
    return JsonResponse(res)

def get_words_monthly(words, birth_date, month_period):
    res = {}
    for month in month_period:
        end_date = birth_date + timedelta(weeks=(month*4))
        period_words = words.filter(date__range=(birth_date, end_date))
        res[month] = {}
        res[month]['count'] = period_words.count()
        res[month]['words'] = [word['base'] for word in period_words.values('base')]
    return res
