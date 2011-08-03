from django.db import models

class Make(models.Model):
    make = models.CharField(max_length = 16)

    def __unicode__(self):
        return self.make

class MakeModel(models.Model):
    make = models.ForeignKey(Make)
    model = models.CharField(max_length = 16)

    class Meta:
        unique_together = ('make', 'model')

    def __unicode__(self):
        return self.make.make + ' ' + self.model

class CarId(models.Model):
    make_model = models.ForeignKey(MakeModel)
    year = models.IntegerField()

