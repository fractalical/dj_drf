from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE,
                                  related_name='measurement')
    temperature = models.FloatField()
    measurement_date = models.DateField(auto_now=True)
    image = models.ImageField(null=True)
