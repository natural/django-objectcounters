#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.translation import ugettext as _


class CounterManager(models.Manager):
    """Manager for the Counter class."""
    def get_for_object(self, name, instance, **kwargs):
        """Given a name and an object, returns the counter instance for it."""
        content_type = ContentType.objects.get_for_model(instance)
        return self.get(name=name, content_type=content_type,
                        object_id=instance.id, **kwargs)

    def get_value_for_object(self, name, instance, default=0, **kwargs):
        """Given a name and an object, returns the counter value for it."""
        try:
            return self.get_for_object(name, instance, **kwargs).value
        except (self.model.DoesNotExist, ):
            return default

    def create_for_object(self, name, instance, value=0):
        """Given a name and an object, get the counter, creating it if necessary."""
        content_type = ContentType.objects.get_for_model(instance)
        counter, created = self.get_or_create(name=name,
            content_type=content_type,
            object_id=instance.id)
        if created:
            counter.value = value
            counter.save()
        return (counter, created)


class Counter(models.Model):
    """Models counters as a simple string and integer pair."""
    name = models.CharField(_('counter name'), max_length=128, db_index=True,
        help_text=_("""Name of the counter"""))
    value = models.BigIntegerField(_('counter value'), default=0,
        help_text=_("""Current value of the counter"""))

    content_type = models.ForeignKey(ContentType, db_index=True, blank=True,
        null=True)
    object_id = models.PositiveIntegerField(db_index=True, blank=True,
        null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = CounterManager()

    class Meta:
        verbose_name = 'Counter'
        unique_together = ('name', 'content_type', 'object_id', )

    def __unicode__(self):
        return unicode(self.name)


class CounterTool(object):
    """Easy access to counters using dynamic attributes and mapping keys.

    Attribute forms:

        >>> counters = CounterTool()
        >>> counters.foo
        0L

        >>> counters.foo = 4
        >>> counters.foo
        4L

        >>> counters.foo += 6
        >>> counters.foo
        10L

    Mapping key forms:

        >>> counters['2012/03/09/photos/uploads/animals']
        0L
        >>> counters['2012/03/09/photos/uploads/animals'] += 1
        >>> counters['2012/03/09/photos/uploads/animals']
        1L

    """
    def __init__(self, model=Counter, default=0):
        self.__dict__.update(model=model, default=default)

    def __getattr__(self, name):
        model = self.model
        try:
            value = model.objects.get(name__exact=name).value
        except (model.DoesNotExist, ):
            value = self.default
        return value

    def __setattr__(self, name, value):
        model = self.model
        try:
            record = model.objects.get(name__exact=name)
        except (model.DoesNotExist, ):
            record = model(name=name)
        record.value = value
        return record.save()

    __getitem__ = __getattr__
    __setitem__ = __setattr__
