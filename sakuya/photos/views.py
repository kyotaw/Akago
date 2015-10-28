from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http.response import JsonResponse
from django.utils.timezone import now
from django.db import IntegrityError

from sakuya.photos.models import Photo
from sakuya.utils import get_active_user, get_owner_child


@csrf_exempt
@require_POST
def upload(request):
#    import pdb; pdb.set_trace()
  
    user = get_active_user(request)
    
    image_file = request.FILES['image_file']
    if not image_file:
        raise Http404

    title = request.POST['title'] if 'title' in request.POST else 'タイトルなし'
    comment = request.POST['comment'] if 'comment' in request.POST else ''

    child = get_owner_child(request, user)
    
    date = now()
    age = child.detail_age()

    try:
        photo = Photo.objects.create(title=title, comment=comment, date=date, image=image_file, age=age, owner=child)
    except IntegrityError:
        raise Http404

    return JsonResponse({})
