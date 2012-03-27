Reporters and Groups
========================
Index
--------
The main reporters view is at webserver/reporters, which accesses the view at `apps.reporters.views.index`

This view retrieves all reporters for which the user has permission, based on the 
UserLocation associated with this user account.  

Further, it uses an optimization, LocationShorthand, to provide easy recursive lookups
within a Location tree mirroring Rwanda's administrative boundaries. 

See :doc:`Models </data_design>` for a more detailed discussion of UserLocation and LocationShorthand,
also see `apps.reporters.views.location_fresher` and `apps.reporters.views.reporter_fresher`
for implementations using these lookups.

Export to CSV
---------------
One additional feature of the reporters app is that it has mirror views for
export to CSV, containing all the same filtering logic, but replacing a 
standard `render_to_response` call with logic for emitting a csv file.

See `apps.reporters.views.*_csv` for examples.

match_inactive
----------------
One important thing to note to avoid confusion is that `match_inactive` is actually
a function used by all the following views (error log, inactive and active reporters),
it simply filters users by location, using LocationShorthand to ease the process.

.. toctree::
   :maxdepth: 2

   active
   inactive
   errorlog