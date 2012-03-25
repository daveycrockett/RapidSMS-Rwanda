Installing and running RapidSMS Rwanda
========================================

Basic Environment Setup
------------------------
If you're already familiar with working on python/Django projects, you'll likely be able to skip this section.  The following steps walk you through the first steps of setting up python, i.e. basic package management and development environments.  This allows you to more easily install the dependencies for RapidSMS-Rwanda, while keeping your base installation of python clean.  This assumes that you already have python installed.

Install easy_install (if necessary)::

    $ wget peak.telecommunity.com/dist/ez_setup.py
    $ python ez_setup.py

Install pip (if necessary)::

    $ easy_install pip

Set up virtualenv, a tool for creating isolated python environments (to keep your dependencies seperate and in local user space, rather than in /usr/)::

    $ pip install virtualenv
    $ pip install virtualenvwrapper

Configure virtualenv.  First, create a folder to organize all your virtual environments within::

    $ mkdir ~/virtualenvs

Append to ~/.bashrc::

    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh

Make the virtual environment::

    $ mkvirtualenv rwanda

Installing RapidSMS-rwanda
----------------------------

First, clone the project directly::

    $ git clone git://github.com/pivotaccess2007/RapidSMS-Rwanda

You can then install the dependencies::

    $ pip install -r pip-requires.txt

Configuring RapidSMS-Rwanda
-----------------------------

The following parameters need to be set in order to get RapidSMS-Rwanda up-and-running from a base install.

First, edit rapidsms.ini and add the basic configuration parameters.  Yours may vary, depending on what sort of database you have, what you want to name it, your time zone, etc.::

    [database]
    engine=django.db.backends.postgresql_psycopg2
    name=rwanda
    user=postgres

    ...
    # Revence thinks this is necessary.
    TIME_ZONE=Africa/Kampala
    BASE_TEMPLATE=layout.html  # This needed to be added

To apps, add `patterns` (this seemed to be missing upon syncdb)::

    apps=webapp,ajax,admin,reporters,locations,messaging,httptester,logger,ubuzima,echo,ambulances,patterns

Create the database::

    $ sudo -u postgres createdb rwanda

Syncdb::

    $ python manage.py syncdb


