from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


# Create your models here.


class Car(models.Model):
    brandname = models.TextField(max_length=60)
    modelname = models.CharField(max_length=60)

    def __str__(self):
        return self.modelname


class CarRate(models.Model):
    rate = models.CharField(max_length=1,
                            validators=[RegexValidator(
                                regex='[1-5]',
                                message='Rate has to be in range 1-5',
                            ),
                            ],

                            )
    carname = models.ManyToManyField(Car)

    def __str__(self):
        return self.rate
