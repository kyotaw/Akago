import os

from PIL import Image
import numpy

from django.core.files import File
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
from sakuya.image_correct import *
from sakuya.settings import MEDIA_ROOT


def get_value(request, key):
    if key in request.POST and request.POST[key] != '':
        value = request.POST[key]
    elif key in request.GET and request.GET[key] != '':
        value = request.GET[key]
    else:
        value = ''
    return value

@csrf_exempt
@require_POST
def upload(request):
#    import pdb; pdb.set_trace()
  
    user = get_active_user(request)
    
    image_file = request.FILES['image_file']
    if not image_file:
        raise Http404
   
    title = get_value(request, 'title')
    if title == '':
        title = 'タイトルなし'
    
    comment = get_value(request, 'comment')
    motion = get_value(request, 'motion')

    child = get_owner_child(request, user)
    
    date = now()
    age = child.detail_age()

    try:
        photo = Photo.objects.create(title=title, audio=None, movie=None, stamp=None, comment=comment, motion=motion, date=date, image=image_file, age=age, owner=child)
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

@require_POST
def convert(request, photo_id):
#    import pdb; pdb.set_trace()
    res = {}

    try:
        photo = Photo.objects.get(id=photo_id)
    except:
        res['status'] = 'error'
        res['reason'] = 'child not found'
        return JsonResponse(res)
        
    if 'effect' not in request.POST and request.POST['effect'] != 'sepia': 
        res['status'] = 'nocoversion'
        return JsonResponse(res)

    file_path, ext = os.path.splitext(photo.image.url)
    out_url = MEDIA_ROOT + file_path + '_sepia' + ext

    img = Image.open(photo.image.path)
    cv_img = numpy.asarray(img)
    cv_new_img = cv_img.copy()

    effect_sepia_raw(cv_img, cv_new_img)
    cv_new_img = cv_new_img[:, :, ::-1].copy()
    new_img = Image.fromarray(cv_new_img)
    new_img.save(photo.image.path)
    
    photo.image.save(photo.image.url, File(open(photo.image.path, 'rb')))
    photo.comment += ' セピアに変換しました。(' + now().strftime('%Y/%m/%d %H:%M:%S') + ')'
    photo.save()

    return JsonResponse(res)
