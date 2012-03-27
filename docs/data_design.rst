Models and Extensions
========================
This page covers an overview of the pertinent models added by the Rwanda customization
of RapidSMS, as well as any extensions made via the ExtensibleModels classes within 
the RapidSMS Framework (Locations, Contacts, Connections, etc).

Locations
------------

LocationShorthand
^^^^^^^^^^^^^^^^^^^^
RapidSMS Locations in version 1.2 suffer from a lack of efficient capabilities for
recursive expansion in the Location tree, having only a simple foreign key to self 
called `parent`.

In order to solve this problem, `apps.ubuzima.models` contains a model,
`LocationShorthand`, which enables this expansion to be looked for any level of
the tree, following a hard-coded structure that mirrors Rwanda's administrative
boundaries that are pertinent to RapidSMS Rwanda, namely district and province.

This allows for simple, fast lookups such as::

    LocationShorthand.objects.filter(district__name='Musanze')
    
Which would return all child Locations of the Musanze district.

The pertinent model implementation is below::

    class LocationShorthand(models.Model):
        'Memoization of locations, so that they are more-efficient in look-up.'

        original = models.ForeignKey(Location, related_name = 'locationslocation')
        district = models.ForeignKey(Location, related_name = 'district')
        province = models.ForeignKey(Location, related_name = 'province')

UserLocation
^^^^^^^^^^^^^^^
Ubuzima also provides a way of mapping web users to the locations they are authorized
to administer, via the UserLocation model::

    class UserLocation(models.Model):
        """This model is used to help the system to know where the user who is trying to access this information is from"""
        user=models.ForeignKey(User)
        location=models.ForeignKey(Location)

Reporters
------------
See `apps.reporters.models`.

Rwanda uses a separate model for known reporters that are validated for submitting
reports within the system.  This model doesn't extend Contact, and is created as a 
result of the registration process.

Further, it uses `PersistantConnection` and `PersistantBackend` models, mirroring
RapidSMS' `Backend` and `Connection` models, but tying in the idea that a single
reporter, using a single phone number (SIM card), could end up communicating over
different backends, depending on the current state of the provider networks and active
SMPP connections.::

    class Reporter(models.Model):
        """This model represents a KNOWN person, that can be identified via
           their alias and/or connection(s). Unlike the RapidSMS Person class,
           it should not be used to represent unknown reporters
           ...
        """   
        alias      = models.CharField(max_length=20, unique=True)
        first_name = models.CharField(max_length=30, blank=True)
        last_name  = models.CharField(max_length=30, blank=True)
        groups     = models.ManyToManyField(ReporterGroup, related_name="reporters", blank=True)
        ...
        location   = models.ForeignKey(Location, related_name="reporters", null=True, blank=True)
        role       = models.ForeignKey(Role, related_name="reporters", null=True, blank=True)
        ...
        village    = models.CharField(max_length=255, null=True)
        
        
Reports
----------
`apps.ubuzima.models` contains a model for taking note of parsing errors
when reporters submit reports::

    class ErrorNote(models.Model):
        '''This model is used to record errors made by people sending messages into the system, to facilitate things like studying which format structures are error-prone, and which reporters make the most errors, and other things like that.'''
        errmsg  = models.TextField()
        errby   = models.ForeignKey(Reporter, related_name = 'erring_reporter')
        created = models.DateTimeField(auto_now_add = True)
        
This model is also used for the "Error Log" view in the `reporters` app.

Finally, all reports consist of the main Report object, and (potentially) any fields
associated with it::

    class Report(models.Model):
        reporter = models.ForeignKey(Reporter)
        location = models.ForeignKey(Location)
        village = models.CharField(max_length=255, null=True)
        fields = models.ManyToManyField(Field)
        patient = models.ForeignKey(Patient)
        type = models.ForeignKey(ReportType)    
        # meaning of this depends on report type..
        # arr, should really do this as a field, perhaps as a munged int?
        date_string = models.CharField(max_length=10, null=True)
    
        # our real date if we have one complete with a date and time
        date = models.DateField(null=True)
    
        created = models.DateTimeField(auto_now_add=True)
        
Because all fields are of numeric type, the Field model is fairly simple::

    class Field(models.Model):
        type = models.ForeignKey(FieldType)
        value = models.DecimalField(max_digits=10, decimal_places=5, null=True)