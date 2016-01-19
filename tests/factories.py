#!/usr/bin/env python
# -*- coding: utf-8 -*-
import factory
from django.conf import settings


class Factory(factory.DjangoModelFactory):

    class Meta:
        strategy = factory.CREATE_STRATEGY
        model = None
        abstract = True


class UserFactory(Factory):

    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: 'user%04d' % n)
    email = factory.Sequence(lambda n: 'user%04d@email.com' % n)
    password = factory.PostGeneration(
        lambda obj, *args, **kwargs: obj.set_password('123123'))

# You can define more fields over here for User Factory as per your custom model
