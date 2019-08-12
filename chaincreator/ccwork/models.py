from django.db import models

# Create your models here.


class contactinfo(models.Model):
    person_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    details_about = models.CharField(max_length=100)
    ifnotin = models.CharField(max_length=100)
    franchise_favour = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    specs_detail = models.TextField(max_length=500)
