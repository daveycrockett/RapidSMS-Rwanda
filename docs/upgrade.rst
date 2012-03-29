Upgrading to the new RapidSMS Core
=====================================

To upgrade to the new RapidSMS core, simply check out the new branch (until it is merged into main)::

    $ git checkout new-rapidsms

A number of database modifications need to occur::

    alter table locations_locationtype add column "slug" varchar(50);
    update locations_locationtype set slug=lower(name);
    alter table locations_locationtype add unique(slug);

    alter table "locations_location" add column "parent_type_id" integer;
    update locations_location set parent_type_id = (select id from django_content_type where model = 'location');
    alter table locations_location add check (parent_id >= 0);
    alter table locations_location add constraint "locations_location_parent_type_id_fkey" foreign key (parent_type_id) references django_content_type(id) deferrable initially deferred;
    alter table locations_location drop constraint parent_id_refs_id_47ca058b;

    CREATE TABLE "locations_point" (
        "id" serial NOT NULL PRIMARY KEY,
        "latitude" numeric(13, 10) NOT NULL,
        "longitude" numeric(13, 10) NOT NULL
    );
    alter table "locations_location" add column "point_id" integer REFERENCES "locations_point" ("id") DEFERRABLE INITIALLY DEFERRED;

    alter table locations_location add column "type_slug" varchar(50) REFERENCES "locations_locationtype" ("slug") DEFERRABLE INITIALLY DEFERRED;

    update locations_location set type_slug = (select slug from locations_locationtype t where t.id = type_id);

    alter table locations_location drop column type_id;

    alter table locations_locationtype drop constraint "locations_locationtype_pkey";

    alter table locations_locationtype drop column id;

    alter table locations_locationtype alter column slug set not null;

    alter table locations_locationtype add constraint locations_locationtype_pkey primary key(slug);

    alter table locations_location rename column type_slug to type_id;

Then, migrate points over to their own class, in shell_plus::

    for l in Location.objects.extra(select={'longitude':'longitude','latitude':'latitude'}).all():
        if l.longitude and l.latitude:
            l.point = Point.objects.create(longitude=l.longitude, latitude=l.latitude)
            l.save()

Finally, drop longitude and latitude from the locations table::

    alter table locations_location drop column latitude;
    alter table locations_location drop column longitude;


