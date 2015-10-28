from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.utils.timezone import now
from django.http.response import JsonResponse

from sakuya.photos.models import Photo


@csrf_exempt
@require_POST
def record(request):
#    import pdb; pdb.set_trace()
    user = None
    if request.user.is_authenticated():
        user = request.user
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        login(request, user)

    if not user or not user.is_active:
        raise Http404

    if 'strength' not in request.POST:
        raise Http404

    strength = request.POST['strength']
    
    child = None
    if 'owner' in request.POST:
        try:
            child = user.child_set.get(name=require_POST['owner'])
        except Child.DoesNotExist:
            raise Http404
    else:
        children = user.child_set.all()
        if not children:
            raise Http404
        child = children[0]
    
    date = now()
    age = child.detail_age()
    footer = 'Strengthからの投稿'
    
    try:
        photo = Photo.objects.create(title=strength, date=date, age=age, owner=child, footer=footer)
    except IntegrityError:
        raise Http404

    return JsonResponse({})
