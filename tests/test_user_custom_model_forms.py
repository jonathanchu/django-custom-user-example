#!/usr/bin/env python
# -*- coding: utf-8 -*-

from customuser.accounts.forms import (CustomUserCreationForm)
import pytest


pytestmark = pytest.mark.django_db


def test_user_custom_model_forms():

    data = {'password1': 'a', 'password2': 'a', 'username': 'user'}
    user_form = CustomUserCreationForm(data)
    assert user_form.is_valid() is True

    data = {'password1': 'a', 'password2': 'b', 'username': 'user'}
    user_form = CustomUserCreationForm(data)
    assert user_form.is_valid() is False

    invalid_data = {'password1': 'a', 'password2': 'a', 'username': 'foqw;efnwldksfalsdkj \
    fosaidfj;alsdfjsadlfkjslakdjfsladkfjslakdjfsdalfkjaslkfaslkdfjaslkdjf'}
    user_form = CustomUserCreationForm(invalid_data)
    assert user_form.is_valid() is False  # Username more than 30 character

# To Add more test for custom forms
