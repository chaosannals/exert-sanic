from tortoise.models import Model
from tortoise import fields

class Tester(Model):
    id=fields.BigIntField(pk=True)
    jobnumber=fields.CharField(8)
    name=fields.CharField(120)
