from django.db import models

class Division(models.Model):
    name = models.CharField(max_length=30) # Measurement lab
    app_name = models.CharField(max_length=20) # meas_lab
    search_form = models.CharField(max_length=30) # meas_lab:search_form

    def __str__(self):
        return self.name

class Code(models.Model):
    division = models.ForeignKey('Division', on_delete=models.CASCADE) # Measurement.lab

    source_id = models.CharField(max_length=30) # L2101
    source_name = models.CharField(max_length=150) # WBC
    target_id = models.CharField(max_length=30) # 21929292
    target_name = models.CharField(max_length=150) # White blood cell [g/mL]
    vocabulary = models.CharField(max_length=30) # LOINC
    domain = models.CharField(max_length=30) # Measurement
    target_concept = models.CharField(max_length=30) # 20192-1
    unit = models.CharField(max_length=30) # g/mL
    review = models.CharField(max_length=250) # default
    other = models.CharField(max_length=100) # ?
   
    def __str__(self):
        return "%s -> %s" % (self.source_id, self.target_id)
