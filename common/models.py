from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


    @property
    def category_name(self):
        return self.category.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='items' ,on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
        
# ----------------------- New Model -------------------- #

class TruckList(models.Model):
    vehicle_no = models.CharField(max_length=50, null=True, blank=True)
    driver_name = models.CharField(max_length=50, null=True, blank=True)
    driver_no = models.CharField(max_length=50, null=True, blank=True)


    def __unicode__(self):
        return self.vehicle_no


    @property
    def truck_list_name(self):
        return self.vehicle_no


class DispatchAdvice(models.Model):
    da_id = models.AutoField(primary_key=True, unique=True)
    jobcode_da_no = models.CharField(max_length=100, null=True)
    da_to = models.CharField(max_length=150, null=True)
    da_cc = models.CharField(max_length=150, null=True)
    da_from = models.IntegerField(null=True)
    da_date = models.DateField(auto_now_add=True, null=True)
    ygs_proj_defi = models.CharField(max_length=150, null=True)
    job_name = models.CharField(max_length=200, null=True)
    job_code = models.CharField(max_length=100, null=True)
    po_date = models.DateField(null=True)

    def __unicode__(self):
        return self.jobcode_da_no


class DATruckList(models.Model):
    truckListID = models.ForeignKey(TruckList, null=True, related_name='truck_list', on_delete=models.CASCADE)
    daID = models.ForeignKey(DispatchAdvice, null=True,related_name='dispath_advice', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, related_name='+', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)