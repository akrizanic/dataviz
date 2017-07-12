=====
Dataviz
=====

Dataviz is a data visualisation app.

Quick start
-----------

1. Add "dataviz" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'dataviz',
    ]

2. Include the dataviz URLconf in your project urls.py like this::

   url(r'^dataviz/', include('dataviz.urls', namespace='dataviz')),

3. Run `python manage.py migrate` to create the dataviz models.

4. Start the development server and visit http://127.0.0.1:8000/dataviz/.

