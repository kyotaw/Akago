from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_GET

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

@require_GET
def query(request, child_id):
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

    monthly = False
    start_month = 0
    if 'start_month' in request.GET:
        start_month = int(request.GET['start_month'])
        monthly = True
    end_month = start_month + 15
    if 'end_month' in request.GET:
        end_month = int(request.GET['end_month'])
        monthly = True

    for pos in get_required_pos(request):
        pos_res = {}
        pos_words = words.filter(pos1=pos[1])
        pos_res['count'] = pos_words.count()
        if pos[0] == 'unk':
            pos_res['words'] = [{ 'word': word['lemma'], 'date': word['date']} for word in pos_words.values('lemma', 'date')]
        else:
            pos_res['words'] = [{ 'word': word['base'], 'date': word['date']} for word in pos_words.values('base', 'date')]
        if monthly:
            pos_res['monthly'] = get_words_monthly(pos, pos_words, birth, range(start_month, end_month + 1))
        res[pos[0]] = pos_res
        
    return JsonResponse(res)

def get_required_pos(request):
    pos_list = []
    for pos in pos_table:
        if pos[0] in request.GET:
            pos_list.append(pos)

    if not pos_list:
        pos_list = pos_table

    return pos_list

def get_words_monthly(pos, words, birth_date, month_period):
    res = {}
    for month in month_period:
        end_date = birth_date + timedelta(weeks=(month*4))
        period_words = words.filter(date__range=(birth_date, end_date))
        res[month] = {}
        res[month]['count'] = period_words.count()
        if pos[0] == 'unk':
            res[month]['words'] = [{ 'word': word['lemma'], 'date': word['date']} for word in period_words.values('lemma', 'date')]
        else:
            res[month]['words'] = [{ 'word': word['base'], 'date': word['date']} for word in period_words.values('base', 'date')]
    return res
