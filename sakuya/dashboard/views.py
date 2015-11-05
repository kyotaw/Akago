from datetime import datetime, timedelta

from django.shortcuts import render
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from sakuya.accounts.models import Child
from sakuya.photos.models import Photo


motion_achive_month_table = {
    'neck_fix': 4,
    'rolling_over': 7,
    'sit': 7,
    'crawl': 10,
    'pullup': 11,
    'standup': 13,
    'walk': 15
}


@login_required
def index(request):
#    import pdb; pdb.set_trace()
    context = {}

    children = request.user.child_set.exclude(name='allofthem')
    context['children'] = children
    
    active_child = children[0] if len(children) > 0 else None
    context['active_child'] = active_child

    context['child_list'] = children[1:]

    try:
        for photo in active_child.photo_set.all():
            if photo.image:
                current_image = photo.image.url
                context['current_image'] = current_image
                break
    except:
        pass;

    for motion in motion_achive_month_table.keys():
        try:
            motion_photo = active_child.photo_set.filter(motion=motion).order_by('date')
            if motion_photo:
                context[motion] = create_motion_text(motion, motion_photo[0].date, active_child.birth)
            else:
                context[motion] = create_motion_text(motion, None, active_child.birth)
        except:
            context[motion] = create_motion_text(motion, None, active_child.birth)
            

    langInfo = {}
    langInfo['n'] = active_child.word_set.filter(pos1='名詞').count()
    langInfo['v'] = active_child.word_set.filter(pos1='動詞').count()
    langInfo['adj'] = active_child.word_set.filter(pos1='形容詞').count()
    langInfo['adv'] = active_child.word_set.filter(pos1='副詞').count()
    langInfo['im'] = active_child.word_set.filter(pos1='感動詞').count()
    langInfo['j'] = active_child.word_set.filter(pos1='助詞').count()
    langInfo['conj'] = active_child.word_set.filter(pos1='接続詞').count()
    langInfo['auv'] = active_child.word_set.filter(pos1='助動詞').count()
    langInfo['p'] = active_child.word_set.filter(pos1='接頭詞').count()
    langInfo['t'] = active_child.word_set.filter(pos1='連体詞').count()
    langInfo['unk'] = active_child.word_set.filter(pos1='未知語').count()
    context['lang'] = langInfo

    all_child_number = Child.objects.count() - 1 # except for all_child
    context['all_child_number'] = all_child_number
    try:
        langMean = {}
        all_child = Child.objects.get(name='allofthem')
        langMean['n'] = all_child.word_set.filter(pos1='名詞').count() // all_child_number
        langMean['v'] = all_child.word_set.filter(pos1='動詞').count() // all_child_number
        langMean['adj'] = all_child.word_set.filter(pos1='形容詞').count() // all_child_number
        langMean['adv'] = all_child.word_set.filter(pos1='副詞').count() // all_child_number
        langMean['im'] = all_child.word_set.filter(pos1='感動詞').count() // all_child_number
        langMean['j'] = all_child.word_set.filter(pos1='助詞').count() // all_child_number
        langMean['conj'] = all_child.word_set.filter(pos1='接続詞').count() // all_child_number
        langMean['auv'] = all_child.word_set.filter(pos1='助動詞').count() // all_child_number
        langMean['p'] = all_child.word_set.filter(pos1='接頭詞').count() // all_child_number
        langMean['t'] = all_child.word_set.filter(pos1='連体詞').count() // all_child_number
        langMean['unk'] = all_child.word_set.filter(pos1='未知語').count() // all_child_number
        context['lang_mean'] = langMean
    except:
        pass

    return render(request, 'dashboard/index.html', Context(context))

def create_motion_text(motion, date, birth):
    if date:
        return date.strftime('%Y/%m/%d') + 'に達成'
    else:
        delta = now() - birth
        years = delta.days // 365
        months = (delta.days - 365 * years) // 31

        remain = motion_achive_month_table[motion] - months
        if 0 < remain:
            return 'だいたい' + str(remain) + 'ヶ月以内'
        else:
            return str(-remain) + 'ヶ月遅れ'


