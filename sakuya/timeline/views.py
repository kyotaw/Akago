from django.shortcuts import render
from django.template import Context
from django.contrib.auth.decorators import login_required

from sakuya.accounts.models import Child, Medal
from sakuya.photos.models import Photo, Stamp

@login_required
def index(request):
#    import pdb; pdb.set_trace()
    
    context = {}

    children = request.user.child_set.exclude(name='allofthem')
    context['children'] = children
    active_child = children[0] if len(children) > 0 else None
    context['active_child'] = active_child
    context['child_list'] = children[1:]

    return render(request, 'timeline/index.html', context)
    
