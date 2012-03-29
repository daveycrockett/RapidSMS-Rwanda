from django.db import models

class NameAndCodeLocation(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=30, null=False)

    class Meta:
        abstract = True
