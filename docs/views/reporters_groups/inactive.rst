Inactive Reporters
======================
The inactive reporters view is at reporters/inactive, which accesses the view at
`apps.reporters.views.view_inactive_reporters`.

Its critical section is in `apps.reporters.views.active_reporters`::

    def inactive_reporters(req,rez):
        active_reps=[]
        reps=Reporter.objects.filter(groups__title='CHW',**rez)
        pst=reporter_fresher(req)
        for rep in reps.filter(**pst):
            if rep.is_expired():
                active_reps.append(rep)
        return active_reps
        
The important method here is `is_expired` in the Reporter model, which iterates
over the `last_seen` attributes of all related PersistantConnections, checking
to see if this reporter has last been seen within the desired date range.

Note that this method is a mirror of `active_reporters` with only a `not` missing 
in the `if rep.is_expired()` branch.

Finally, this view chains to location_fresher, only returning those reporters
that the user has authorization to view.

