# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from tiger.base import routers
from django.conf import settings

router = routers.DefaultRouter(trailing_slash=False)

# Locales
from tiger.locale.api import LocalesViewSet

router.register(r"locales", LocalesViewSet, base_name="locales")


# Users & Roles
from tiger.auth.api import AuthViewSet
from tiger.users.api import UsersViewSet
from tiger.users.api import RolesViewSet

router.register(r"auth", AuthViewSet, base_name="auth")
router.register(r"users", UsersViewSet, base_name="users")
router.register(r"roles", RolesViewSet, base_name="roles")

