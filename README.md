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
    Counter.objects.create_for_object('friends_total', capt, 1014)

And:

    last = Counter.objects.get_for_object('friends_last_month', capt)
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

To run the sample app, make sure you've got generic admin installed globally
(ugh), or better yet, create a new virtual env and install it there with the
sample.


Python Usage
-------------

The `Counter` model is a regular Django model, so you can create, read, update
and delete records in the usual way.  Additionally, the model provides a manager
with a few more methods:

1.  `Counter.get_for_object(name, instance, **kwargs)`

Use this method to get an existing counter for an object.  Pass in the name of
the counter, like 'total-holodeck-hours', and a model instance.  Keyword
arguments are passed thru to the `get()` call.

2.  `Counter.get_value_for_object(self, name, instance, default=0, **kwargs)`

Use this method when you need just the value of a counter and not the counter
record.  Keyword arguments are passed thru to the `get()` call.

3.  `Counter.create_for_object(self, name, instance, value=0)`

This is just like Django's `get_or_create` and returns the same kind of
two-tuple.  Use this when you need to get a counter and create it if necessary
in one step.



Template Usage
--------------

You can also enable counters inside of templates pretty easily.


1.  In your templates, load the tag:

  {% load counter_tags %}

2.  Then you can render values like this:

  <span>
    {% counter_for_object "monthly_shack_visits" user as visits %}
    I went to Shake Shack {{ visits }} times this month.
  </span>
