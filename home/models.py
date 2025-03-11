# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User_In_Testing(models.Model):

    #__User_In_Testing_FIELDS__
    test_name_user = models.CharField(max_length=255, null=True, blank=True)
    blahblah = models.CharField(max_length=255, null=True, blank=True)

    #__User_In_Testing_FIELDS__END

    class Meta:
        verbose_name        = _("User_In_Testing")
        verbose_name_plural = _("User_In_Testing")


class Test_Other_Model(models.Model):

    #__Test_Other_Model_FIELDS__
    blah_blah_blah = models.ForeignKey(User_In_Testing, on_delete=models.CASCADE)
    fitness_gram_pacer_test = models.CharField(max_length=255, null=True, blank=True)

    #__Test_Other_Model_FIELDS__END

    class Meta:
        verbose_name        = _("Test_Other_Model")
        verbose_name_plural = _("Test_Other_Model")



#__MODELS__END
