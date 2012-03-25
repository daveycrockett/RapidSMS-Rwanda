Error Log
============
The inactive reporters view is at reporters/errors, which accesses the view at
`apps.reporters.views.error_list`.

This view looks for appropriate location, filtered by UserLocation, and then 
looks for `apps.ubuzima.models.ErrorNote` objects associated with each reporter
location and within the appropriate time ranges::

    if 'location__id' in l.keys(): rez['errby__location__id']=l['location__id']
    elif 'location__in' in l.keys(): rez['errby__location__in']=l['location__in']
    elif 'location__id' in pst.keys():  ps['errby__location__id']=pst['location__id']
    elif 'location__in' in pst.keys():  ps['errby__location__in']=pst['location__in']
    try:
        rez['created__gte'] = filters['period']['start']
        rez['created__lte'] = filters['period']['end']+timedelta(1)
    except KeyError:
        pass
    errs=ErrorNote.objects.filter(**rez).order_by('-created')


