Object Counters for Django
==========================

This is a simple app for associating named integer values with
arbitrary Django model objects.

Using counters allows you to keep scalar values out of your models.
Instead of this:

    class Person(models.Model):
        name = models.CharField(...)
        number_of_friends_total = models.IntegerField(...)
        number_of_friends_recent = models.IntegerField(...)
        number_of_friends_last_month = models.IntegerField(...)

You can do this:

    capt = Person(name='Jean-Luc Picard')
    Counters.create_for_object('friends_total', capt, 1014)

And:

    last = Counters.get_for_object('friends_last_month', capt)
    last.value += -3 # lost the away team.
    last.save()

The approach of reading and writing values in a separate model allows
you to evolve some of your data without touching the models.  And it
keeps your models a bit more tidy.

Install
-------

Pull down the app:

    $ pip install django-objectcounters

Add it to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
      ...
      'objectcounters'
    )

Sync your database:

  $ ./manage.py syncdb --migrate


Usage
-----

