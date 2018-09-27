# -*- coding: utf-8 -*-

from smoke_backend.models import Privilege
from smoke_backend.extensions import ma, db
from smoke_backend.commons.pagination import paginate


class PrivilegeSchema(ma.ModelSchema):

    class Meta:
        model = Privilege
