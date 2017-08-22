# -*- coding: utf-8 -*-

from peewee import CharField, PrimaryKeyField, IntegerField, CompositeKey

from .. import BaseModel


class Blueprint(BaseModel):
    id = PrimaryKeyField()
    blueprint = CharField(unique=True, null=False)
    name = CharField(unique=True, null=False)

    class Meta:
        db_table = 'blueprint'


class Permission(BaseModel):
    id = PrimaryKeyField()
    endpoint = CharField(unique=True, null=False)
    blueprint_id = IntegerField(null=False)

    class Meta:
        db_table = 'permission'


class PermissionGroup(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True, null=False)
    blueprint_id = IntegerField(null=False)

    class Meta:
        db_table = 'permission_group'


class PermissionAllocation(BaseModel):
    permission_id = IntegerField(null=False)
    # permission group id
    pgroup_id = IntegerField(null=False)

    class Meta:
        primary_key = CompositeKey('permission_id', 'pgroup_id')
        db_table = 'permission_allocation'


class Role(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True, null=False)

    class Meta:
        db_table = 'role'


class PermissionGroupAllocation(BaseModel):
    role_id = IntegerField(null=False)
    # permission group id
    pgroup_id = IntegerField(null=False)

    class Meta:
        primary_key = CompositeKey('role_id', 'pgroup_id')
        db_table = 'permission_group_allocation'
