from django.db import models

class NameAndCodeLocation(models.Model):
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=30, null=False)

    @property
    def latitude(self):
        return self.point.latitude if self.point else None

    @property
    def longitude(self):
        return self.point.longitude if self.point else None

    class Meta:
        abstract = True
