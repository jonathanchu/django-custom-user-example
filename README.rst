==========================
Django Custom User Example
==========================

This is an example Django project that demonstrates the configurable User model available in Django 1.5.  It is inspired by `Dr. Russell Keith-Magee's <https://github.com/freakboy3742>`_ talk at DjangoCon US 2013 `Red User, Blue User, MyUser, auth.User <https://speakerdeck.com/freakboy3742/red-user-blue-user-myuser-auth-dot-user>`_.

Getting Started
---------------
Clone this repository:
::

    $ git clone https://github.com/jonathanchu/django-custom-user-example.git
    $ cd django-custom-user-example

Create a virtual environment for this project and install Django (1.5.4 recommended):
::

    $ mkvirtualenv customuser
    (customuser) $ pip install django

Run `syncdb` and create a superuser when prompted:
::

    (customuser) $ python manage.py syncdb
    ...

Run `runserver`:
::

    (customuser) $ python manage.py runserver

Finally, open up http://127.0.0.1:8000/admin in your browser and login with the superuser just created.  You should see your custom user under "Accounts".

Screenshots
-----------

.. image::

Comments/Feedback
-----------------

Suggestions for any modifications, please feel free to fork and contribute!

Please file bugs at `https://github.com/jonathanchu/django-custom-user-example/issues <https://github.com/jonathanchu/django-custom-user-example/issues>`_.
