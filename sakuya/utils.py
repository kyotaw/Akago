from django.http import Http404

def get_active_user(request):
    if request.user.is_authenticated():
        return request.user
    else:
        username = request.POST['username'] if 'username' in request.POST else request.GET['username']
        password = request.POST['password'] if 'password' in request.POST else request.GET['password']
        if username == None or password == None:
            raise Http404

        user = authenticate(username=username, password=password)
        login(request, user)
        return user

def get_owner_child(request, user):
    child = None

    if 'owner' in request.GET:
        try:
            child = user.child_set.get(name=request.GET['owner'])
        except Child.DoesNotExist:
            raise Http404
    elif 'owner' in request.POST:
        try:
            child = user.child_set.get(name=request.POST['owner'])
        except Child.DoesNotExist:
            raise Http404
    else:
        children = user.child_set.all()
        if not children:
            raise Http404
        child = children[0]
    
    if child == None:
        raise Http404

    return child
