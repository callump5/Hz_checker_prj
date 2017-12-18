# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stars(models.Model):
    star_name = models.CharField(max_length=50)
    hip_name = models.CharField(max_length=50)
    hd_name = models.CharField(max_length=50)
    gj_name = models.CharField(max_length=50)

    planets_in_system = models.IntegerField()

    distance = models.FloatField()
    distance_plus = models.FloatField(null=True)
    distance_minus = models.FloatField(null=True)

    v_band_mag = models.FloatField()
    v_band_mag_plus = models.FloatField(null=True)
    v_band_mag_minus = models.FloatField(null=True)

    b_v_mag = models.FloatField()
    b_v_mag_plus = models.FloatField(null=True)
    b_v_mag_minus = models.FloatField(null=True)

    spectral_type = models.CharField(max_length=10)

    stellar_bm_lumo = models.FloatField()
    stellar_bm_lumo_plus = models.FloatField(null=True)
    stellar_bm_lumo_minus = models.FloatField(null=True)