from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# User model
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
        except:
            emailField = ''

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
        except:
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


    @staticmethod
    def validateRecoveryJsonObject(jsonObject):
        try:
            emailField = jsonObject['email']
            emailField = emailField.lower()
        except:
            emailField = ''

        if emailField == '':
            return {'code': 'account/noemail'}, 404

        # Validate values of fields
        try:
            validate_email(emailField)
        except ValidationError:
            return {'code': 'account/wrongemail'}, 404

        return {'code': 'ok'}, 200


    @staticmethod
    def validateResetpasswordJsonObject(jsonObject):
        try:
            codeField = jsonObject['code']
            codeField = codeField.lower()
        except:
            codeField = ''
        try:
            passwordField = jsonObject['password']
        except KeyError:
            passwordField = ''

        if codeField == '':
            return {'code': 'account/nocode'}, 404

        if passwordField == '':
            return {'code': 'account/nopassword'}, 404

        return {'code': 'ok'}, 200

    def updateFromJsonObject(self, jsonObject):
        try:
            emailField = jsonObject['email']
            emailField = emailField.lower()
        except:
            emailField = ''
        try:
            passwordField = jsonObject['password']
        except KeyError:
            passwordField = ''
        try:
            first_nameField = jsonObject['firstname']
        except KeyError:
            first_nameField = ''
        try:
            last_nameField = jsonObject['lastname']
        except KeyError:
            last_nameField = ''

        if emailField != '':
            self.email = emailField

        if passwordField != '':
            self.set_password(passwordField)

        if first_nameField != '':
            self.first_name = first_nameField

        if last_nameField != '':
            self.last_name = last_nameField

        return {'code': 'ok'}, 200


# Code model
class Code(models.Model):
    text = models.TextField(max_length=512)
    type = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField('date created', auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField('date updated', auto_now=True, blank=True, null=True)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
