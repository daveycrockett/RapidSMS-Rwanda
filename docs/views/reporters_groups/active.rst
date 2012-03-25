Active Reporters
=================
The active reporters view is at reporters/active, which accesses the view at
`apps.reporters.views.view_active_reporters`.

Its critical section is in `apps.reporters.views.active_reporters`::

    def active_reporters(req,rez):
        active_reps=[]
        reps=Reporter.objects.filter(groups__title='CHW',**rez)
        pst=reporter_fresher(req)
        for rep in reps.filter(**pst):
            if not rep.is_expired():
                active_reps.append(rep)
        return active_reps
        
The important method here is `is_expired` in the Reporter model, which iterates
over the `last_seen` attributes of all related PersistantConnections, checking
to see if this reporter has last been seen within the desired date range.

Finally, this view chains to location_fresher, only returning those reporters
that the user has authorization to view.