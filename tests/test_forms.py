"""This tests the forms.py"""
import pytest
from gatorgrouper.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
    UploadCSVForm,
    CreateGroupForm,
)
from mixer.backend.django import mixer
from gatorgrouper import models
from django.contrib.auth import get_user_model


pytestmark = pytest.mark.django_db


class TestCustomUserCreationForm:
    "undocumented"
    # pylint: disable=too-few-public-methods
    # pylint: disable=R0201
    def test_valid_data(self):
        """undocumented"""
        form = CustomUserCreationForm(
            {
                "email": "testuserl@test.com",
                "first_name": "Spencer",
                "last_name": "Huang",
                "password1": "testpassword1",
                "password2": "testpassword1",
            }
        )
        assert form.is_valid() is True


class TestCustomUserChangeForm:
    """undocumented"""

    # pylint: disable=too-few-public-methods
    # pylint: disable=R0201
    def test_valid_data(self):
        """undocumented"""
        User = get_user_model()
        user = User.objects.create_user(email="normaluser@user.com", first_name="testfirst", last_name="testlast", password="testpassword")
<<<<<<< HEAD
        data = {
            'email': user.email,
            'first_name': 'testfirst',
            'last_name': 'testlast',
            'password': 'testpassword',
        }
        form = CustomUserChangeForm(data, instance=user)
=======
        form = CustomUserChangeForm(
            {
                'email': 'normaluser@user.com',
                'first_name': 'testfirst',
                'last_name': 'testlast',
                # 'password': 'testpassword',
            }
            , instance=user
        )
>>>>>>> 8fe81fdaf00d27045757d66368fb90aa9ee936e7
        assert form.is_valid() is True


class TestUploadCSVForm:
    """undocumented"""

    # pylint: disable=too-few-public-methods
    # pylint: disable=R0201
    def test_valid_data(self, generate_csv):
        """undocumented"""
        form = UploadCSVForm({"file": generate_csv, "numgrp": 3})
        assert (
            form.fields["preferences_weight"].label
            == "Importance of an unmatched preference"
        )
        assert form.fields["numgrp"].label == "Number of groups to create"
        assert (
            form.fields["preferences_weight_match"].label
            == "Importance of a matched preference"
        )


class TestCreateGroupForm:
    """undocumented"""

    # pylint: disable=too-few-public-methods
    # pylint: disable=R0201
    def test_valid_data(self):
        """undocumented"""
        form = CreateGroupForm({"numgrp": 3})
        assert form.fields["numgrp"].label == "Number of groups to create"
