# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..authentication_app.models import *

class CarManager(models.Manager):
    def Validate(self, RequestPost):
        results = { 'status' : True, 'errors' : [], 'ThisCar' : None }
        user_id = RequestPost['User_Id']

        make = RequestPost['make']
        if (len(make) < 3):
            results['errors'].append("make '{}' is too short, you need atleast 3 characters".format(make) )
        if (len(make) > 100):
            results['errors'].append("make '{}' is too long, you need atmost 100 characters".format(make) )

        model = RequestPost['model']
        if (len(model) < 3):
            results['errors'].append("model '{}' is too short, you need atleast 3 characters".format(model) )
        if (len(model) > 100):
            results['errors'].append("model '{}' is too long, you need atmost 100 characters".format(model) )

        year = RequestPost['year']
        if (len(year) < 3):
            results['errors'].append("year '{}' is too short, you need atleast 3 characters".format(year) )
        if (len(year) > 4):
            results['errors'].append("year '{}' is too long, you need atmost 4 characters".format(year) )

        numberYear = int(year)
        if numberYear < 1900:
            results['errors'].append("year '{}' is too small, you cannot save a year before 1900.".format(numberYear) )
        if numberYear > 2050:
            results['errors'].append("year '{}' is too large, you cannot save a year after 2050.".format(numberYear) )

        #Done with validation
        results['status'] = (0 == len(results['errors'] ) )
        print results['errors']
        return results

    def Creator(self, RequestPost):
        result = self.Validate(RequestPost)
        if (True == result['status'] ):
            newCar = Car.objects.create(
                Make = RequestPost['make'],
                Model = RequestPost['model'],
                Year = RequestPost['year'],
                OwnerId = int(RequestPost['User_Id']),
            )
            newCar.save()
            result['ThisCar'] = newCar
        return result


class Car(models.Model):
    Make = models.CharField(max_length = 100)
    Model = models.CharField(max_length = 100)
    Year = models.CharField(max_length = 10)
    OwnerId = models.IntegerField(default=0)
    objects = CarManager()

    def __str__(self):
        return "{} {} {} {}".format(self.OwnerId, self.Make, self.Model, self.Year)
