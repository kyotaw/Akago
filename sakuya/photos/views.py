from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.http.response import JsonResponse
from django.utils.timezone import now
from django.db import IntegrityError

from sakuya.photos.models import Photo
from sakuya.accounts.models import Child
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

@require_GET
def query(request, child_id):
    res = {}
    
    try:
        child = Child.objects.get(id=child_id)
    except:
        res['status'] = 'error'
        res['reason'] = 'child not found'
        return JsonResponse(res)

    photo_list = []
    photos = child.photo_set.all()
    for photo in photos:
        photo_res = {}
        photo_res['title'] = photo.title
        photo_res['image'] = photo.image.url if photo.image else ''
        photo_res['audio'] = 'media/' + photo.audio.url if photo.audio else ''
        photo_res['movie'] = photo.movie.url if photo.movie else ''
        photo_res['date'] = photo.date.strftime('%Y/%m/%d %H:%M:%S')
        photo_res['age'] = photo.age
        photo_res['comment'] = photo.comment
        photo_res['owner_id'] = photo.owner.id
        photo_res['stamp'] = photo.stamp.image.url if photo.stamp and photo.stamp.image else ''
        photo_res['footer'] = photo.footer
        photo_res['motion'] = photo.motion
        photo_res['id'] = photo.id
        photo_list.append(photo_res) 
    res['photos'] = photo_list
    return JsonResponse(res)
