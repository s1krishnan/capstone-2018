# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100, null=False)
    industry = models.TextField(max_length=200, null=True)
    org_name = models.TextField(max_length=300, null=False)
    user_pk = models.CharField(max_length=50, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class CompanyDimensionTable(models.Model):
    company_id = models.CharField(primary_key=True, max_length=50)
    company_name = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    state_code = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zipcode = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    no_of_funding_rounds = models.IntegerField(blank=True, null=True)
    total_funding_received = models.TextField(blank=True, null=True)
    founded_date = models.TextField(blank=True, null=True)
    employee_count = models.TextField(blank=True, null=True)
    mgmt_01 = models.TextField(blank=True, null=True)
    mgmt_02 = models.TextField(blank=True, null=True)
    mgmt_03 = models.TextField(blank=True, null=True)
    mgmt_04 = models.TextField(blank=True, null=True)
    mgmt_05 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_dimension_table'


class FundingRoundDimension(models.Model):
    funding_round_id = models.CharField(primary_key=True, max_length=50)
    company_id = models.CharField(max_length=50)
    round_type = models.TextField(blank=True, null=True)
    lead_investor_id = models.CharField(max_length=50)
    other_investor_1 = models.TextField(blank=True, null=True)
    other_investor_2 = models.TextField(blank=True, null=True)
    other_investor_3 = models.TextField(blank=True, null=True)
    other_investor_4 = models.TextField(blank=True, null=True)
    other_investor_5 = models.TextField(blank=True, null=True)
    other_investor_6 = models.TextField(blank=True, null=True)
    other_investor_7 = models.TextField(blank=True, null=True)
    other_investor_8 = models.TextField(blank=True, null=True)
    other_investor_9 = models.TextField(blank=True, null=True)
    other_investor_10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding_round_dimension'
        unique_together = (('funding_round_id', 'company_id', 'lead_investor_id'),)


class InvestorsDimensionsTableFinal(models.Model):
    investor_id = models.CharField(primary_key=True, max_length=50)
    investor_name = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    state_code = models.TextField(blank=True, null=True)
    region = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    zip_code = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    founded_date = models.TextField(blank=True, null=True)
    investor_type = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    investment_count = models.IntegerField(blank=True, null=True)
    total_funding_usd = models.TextField(blank=True, null=True)
    mgmt_01 = models.TextField(blank=True, null=True)
    mgmt_02 = models.TextField(blank=True, null=True)
    mgmt_03 = models.TextField(blank=True, null=True)
    mgmt_04 = models.TextField(blank=True, null=True)
    mgmt_05 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investors_dimensions_table_final'


class TimeDimensionTable(models.Model):
    date_id = models.CharField(primary_key=True, max_length=50)
    date = models.TextField(blank=True, null=True)
    year = models.TextField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    day = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'time_dimension_table'


class FundingFactTable(models.Model):
    funding_round_id = models.ForeignKey('FundingRoundDimension', models.DO_NOTHING)
    company_id = models.ForeignKey('CompanyDimensionTable', models.DO_NOTHING)
    lead_investor_id = models.ForeignKey('InvestorsDimensionsTableFinal', models.DO_NOTHING)
    date_id = models.ForeignKey('TimeDimensionTable', models.DO_NOTHING)
    amount_raised = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funding_fact_table'
        unique_together = (('funding_round_id', 'company_id', 'lead_investor_id', 'date_id'),)
