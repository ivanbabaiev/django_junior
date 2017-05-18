# -*- coding: utf-8 -*-

from django.db import models


class TestingSection(models.Model):
    test = models.CharField(max_length=255)

    def __unicode__(self):
        return self.test


class Questions(models.Model):
    section = models.CharField(max_length=255)

    def __unicode__(self):
        return self.section


class Answers(models.Model):
    address = models.CharField(max_length=255)

    def __unicode__(self):
        return self.address


class Test(models.Model):
    pass
