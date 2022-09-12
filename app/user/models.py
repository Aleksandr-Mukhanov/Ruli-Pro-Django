from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from app.mixins.db_classes import NameMixin, CreatedUpdatedMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, NameMixin, CreatedUpdatedMixin):
    phone = models.CharField(_('phone'), unique=True, max_length=12)
    surname = models.CharField(_('surname'), max_length=30, blank=True)
    patronymic = models.CharField(_('patronymic'), max_length=30, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name="Админ")

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        # Возвращает surname и name с пробелом между ними.
        full_name = '%s %s' % (self.surname, self.name)
        return full_name.strip()

    def get_short_name(self):
        # Возвращает сокращенное имя пользователя.
        return self.name
