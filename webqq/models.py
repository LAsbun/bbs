from django.db import models
from app01 import models as bbs_models
# Create your models here.

class QQGroup(models.Model):
    name = models.CharField(max_length=64)
    founder = models.ForeignKey(bbs_models.Admin)
    brief = models.TextField(max_length=1024,default='nothing...')

    admin = models.ManyToManyField(bbs_models.Admin, related_name='group_admin')

    member  =models.ManyToManyField(bbs_models.Admin, related_name='group_members')

    member_limit = models.IntegerField(default=200)

    def __unicode__(self):
        return self.name