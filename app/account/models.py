from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class User(AbstractUser):

    def getUserData(self):

        roles = []

        if self.is_staff:
            roles.append('user')
        if self.is_superuser:
            roles.append('admin')

        if len(roles) == 0:
            return {}

        return {
                "id": self.id,
                "username": self.username,
                "email": self.email,
                "firstname": self.first_name,
                "lastname": self.last_name,
                "roles": roles
            }

    @staticmethod
    def validateProfileUpdateJsonObject(jsonObject):

        try:
            emailField = jsonObject['email']
            emailField = emailField.lower()
        except KeyError:
            emailField = ''
        try:
            passwordField = jsonObject['password']
        except KeyError:
            passwordField = ''

        if emailField == '':
            return {'code': 'account/noemail'}, 404

        # Validate values of fields
        try:
            validate_email(emailField)
        except ValidationError:
            return {'code': 'account/wrongemail'}, 404

        return {'code': 'ok'}, 200

    @staticmethod
    def validateLoginJsonObject(jsonObject):
        try:
            emailField = jsonObject['email']
            emailField = emailField.lower()
        except KeyError:
            emailField = ''
        try:
            passwordField = jsonObject['password']
        except KeyError:
            passwordField = ''

        if emailField == '':
            return {'code': 'account/noemail'}, 404

        if passwordField == '':
            return {'code': 'account/nopassword'}, 404

        # Validate values of fields
        try:
            validate_email(emailField)
        except ValidationError:
            return {'code': 'account/wrongemail'}, 404

        return {'code': 'ok'}, 200


    def updateFromJsonObject(self, jsonObject):
        try:
            emailField = jsonObject['email']
            emailField = emailField.lower()
        except KeyError:
            emailField = ''
        try:
            passwordField = jsonObject['password']
        except KeyError:
            passwordField = ''
        try:
            self.first_name = jsonObject['firstname']
        except KeyError:
            self.first_name = ''
        try:
            self.last_name = jsonObject['lastname']
        except KeyError:
            self.last_name = ''

        self.email = emailField
        if passwordField != '':
            self.set_password(passwordField)

        return {'code': 'ok'}, 200