from django.shortcuts import render
from django.template import Context
from django.contrib.auth.decorators import login_required

from sakuya.accounts.models import Child
from sakuya.photos.models import Photo

@login_required
def index(request):
#    import pdb; pdb.set_trace()
    
    children = request.user.child_set.all()
    active_child = children[0] if len(children) > 0 else None

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

    context = Context({ 'children': children, 'active_child': active_child, 'lang': langInfo })

    return render(request, 'dashboard/index.html', context)
