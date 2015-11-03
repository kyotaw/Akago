from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.http.response import JsonResponse

from sakuya.photos.models import Photo, Stamp
from sakuya.strength.models import Muscle
from sakuya.accounts.models import Child
from sakuya.utils import get_active_user, get_owner_child


@csrf_exempt
@require_POST
def record(request):
#    import pdb; pdb.set_trace()
    user = get_active_user(request)

    if 'strength' not in request.POST:
        raise Http404

    strength = request.POST['strength']
    
    child = get_owner_child(request, user)
    try:
        child.muscle_set.create(strength=strength, date=now())
    except:
        raise Http404

    try:
        all_child = Child.objects.get(id=4)
        all_child.muscle_set.create(strength=float(strength), date=now())
    except:
        raise Http404
    
    title = strength + 'ニュートン'
    age = child.detail_age()
    footer = 'Strengthからの投稿'
    comment = ''

    high_score = False
    records = child.muscle_set.filter(strength__gt=float(strength))
    if not records:
       high_score = True
       comment = '新記録！'
    
    try:
        photo = Photo.objects.create(title=title, date=now(), age=age, owner=child, comment=comment, footer=footer)
        if high_score:
            try:
                stamp = Stamp.objects.get(title='VeryGood')
                photo.stamp = stamp
                photo.save()
            except:
                pass
    except IntegrityError:
        raise Http404

    return JsonResponse({})


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
    
    monthly = False
    start_month = 0
    if 'start_month' in request.GET:
        start_month = int(request.GET['start_month'])
        monthly = True
    end_month = start_month + 15
    if 'end_month' in request.GET:
        end_month = int(request.GET['end_month'])
        monthly = True
    
    start_date = child.birth + timedelta(weeks=(start_month*4))
    end_date = child.birth + timedelta(weeks=(end_month*4))

    muscle_res = {}
    records = child.muscle_set.filter(strength__gte=0.0, date__range=(start_date, end_date))
    muscle_res['count'] = records.count()
    muscle_res['values'] = []
    for muscle in records.values('strength', 'date'):
        delta = muscle['date'] - child.birth 
        years = delta.days // 365
        months = (delta.days - 365 * years) // 31
        days = delta.days - 365 * years - 31 * months
        muscle_res['values'].append({'value': muscle['strength'], 'years': years, 'months': months, 'days': days})
#    if monthly:
#        muscle_res['monthly'] = get_muscle_monthly(muscle, records, child.birth, range(start_month, end_month + 1))
    res['strength'] = muscle_res
    res['status'] = 'success'

    return JsonResponse(res)


def get_muscle_monthly(muscle, records, birth_date, month_period):
    res = {}
    for month in month_period:
        end_date = birth_date + timedelta(weeks=(month*4))
        period_records = records.filter(date__range=(birth_date, end_date))
        res[month] = {}
        res[month]['count'] = period_records.count()
        res[month]['values'] = []
        for muscle in period_records.values('strength', 'date'):
            delta = muscle['date'] - birth_date
            years = delta.days // 365
            months = (delta.days - 365 * years) // 31
            days = delta.days - 365 * years - 31 * months
            res[month]['values'].append({'value': muscle['strength'], 'years': years, 'months': months, 'days': days})
    return res
