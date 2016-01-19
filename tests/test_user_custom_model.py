#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .factories import UserFactory
from customuser.accounts.models import CustomUser
import pytest


pytestmark = pytest.mark.django_db


def test_user_custom_model():
    user = UserFactory.create(username="sampleuser")
    assert user.username == "sampleuser"
    assert user.is_staff is False
    assert user.is_superuser is False

# You Can Add More Test Case w.r.t to your custom model


def test_custom_model_required_fields():
    user = CustomUser(username="user")
    user.save()
    # assert user.is_valid() is False
