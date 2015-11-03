from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.http import require_GET

from sakuya.accounts.models import Child


motion_list = [
  'neck_fix',
  'rolling_over',
  'sit',
  'crawl',
  'pullup',
  'standup',
  'walk'
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

    for motion in get_required_motion(request):
        motion_res = {}
        try:
            photos = child.photo_set.filter(motion=motion)
            motion_res['count'] = photos.count()
            motion_res['image_urls'] = []
            for photo in photos:
                motion_res['image_urls'].append(photo.image.url)
        except:
            motion_res['count'] = 0
            motion_res['image_urls'] = []
        
        res[motion] = motion_res

    res['status'] = 'success'
    return JsonResponse(res)
   

def get_required_motion(request):
    required_motion = []
    for motion in motion_list:
        if motion in request.GET:
            required_motion.append(motion)

    if not required_motion:
        required_motion = motion_list

    return required_motion
        
