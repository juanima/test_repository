


@login_required
def looks_sure(request, id):

    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)

    if valid_data['user_id'] != id:
        stringResponse = {'detail':'Unauthorized Request'}
        return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

    project_obj = get_object_or_404(Project, pk=int(id))


def get_object_or_404(klass, *args, **kwargs):
    query_set = _get_query_set(klass)

    if not hashattr(queryset, 'get'):
        klass_name = klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        raise ValueError("First arguments must be a Modelo, not" % klass_name)

    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise Http404('No %s matches the given query' % queryset.model._meta.object_name)



