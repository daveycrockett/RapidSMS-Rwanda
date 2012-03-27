SMS Messaging Logic
=====================

The SMS messaging logic for the RapidSMS project is all housed within a monolithic app
within `apps.ubuzima.App`.  It uses the keyworder parser and several handler methods
to handle customized parsing for each message type, with validation and parsing logic
interspersed throughout each message type's method, as well as creation of any
supplemental models or reports based on the type of message.

Additionally, this is where `ErrorNote` objects are created when an erroneous 
message is encountered.

One critical portion of the logic is the `create_report` method, invoked by
the majority of the handler methods to create the `Report` object associated 
with the message.  See :doc:`Models </data_design>` for a more detailed description
of `Report` and `Field` objects.  The `create_report` method is as follows::

    def create_report(self, report_type_name, patient, reporter):
        """Convenience for creating a new Report object from a reporter, 
        patient and type """
        
        report_type = ReportType.objects.get(name=report_type_name)
        report = Report(patient=patient, reporter=reporter, type=report_type,
                        location=reporter.location, village=reporter.village)
        return report

The individual message types are described below.

Registration messages
------------------------
Registration messages are of the form:: 
    
    SUP YOUR_ID CLINIC_ID LANG VILLAGE
    or
    REG YOUR_ID CLINIC_ID LANG VILLAGE
    
Depending on if the user's role is 'Supervisor' or 'CHW', respectively. This
message updates or creates an associated `Reporter` object, and no reports.

Pregnancy Messages
---------------------
Pregnancy registrations are of the form::

    PRE MOTHER_ID LAST_MENSES ACTION_CODE LOCATION_CODE MOTHER_WEIGHT
    
Only registered reporters are allowed to send this message, and a correct message
sent from a registered reporter creates a Report object of type 'Pregnancy', with any
associated Field objects.

