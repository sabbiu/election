# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    address_id = models.IntegerField(db_column='Address_id', primary_key=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    vdc_municipality = models.CharField(db_column='VDC_Municipality', max_length=50)  # Field name made lowercase.
    wardno = models.CharField(db_column='WardNo', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Citizenship(models.Model):
    citizenship_id = models.CharField(db_column='Citizenship_id', primary_key=True, max_length=20)  # Field name made lowercase.
    citizenshiptype = models.CharField(db_column='CitizenshipType', max_length=20)  # Field name made lowercase.
    birthdistrict = models.CharField(db_column='BirthDistrict', max_length=20)  # Field name made lowercase.
    issuedate = models.DateField(db_column='IssueDate')  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    issuedaddress = models.ForeignKey(Address, models.DO_NOTHING, db_column='IssuedAddress_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Citizenship'


class Disability(models.Model):
    disability_id = models.CharField(db_column='Disability_id', primary_key=True, max_length=5)  # Field name made lowercase.
    disabilitydescription = models.CharField(db_column='DisabilityDescription', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disability'


class VoterInfo(models.Model):
    voter_id = models.IntegerField(db_column='Voter_id', primary_key=True)  # Field name made lowercase.
    citizenship = models.ForeignKey(Citizenship, models.DO_NOTHING, db_column='Citizenship_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
    spousename = models.CharField(db_column='SpouseName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=50)  # Field name made lowercase.
    grandfathername = models.CharField(db_column='GrandFatherName', max_length=50)  # Field name made lowercase.
    mothertongue = models.CharField(db_column='MotherTongue', max_length=50)  # Field name made lowercase.
    mobile = models.CharField(db_column='Mobile', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    literacystatus = models.CharField(db_column='LiteracyStatus', max_length=1)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.ForeignKey(Address, models.DO_NOTHING, db_column='Address_id')  # Field name made lowercase.
    disability = models.ForeignKey(Disability, models.DO_NOTHING, db_column='Disability_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Voter_info'
