"""
Serializers for the STIXGen project.

This module provides serializers for converting STIX bundle model instances
to JSON format and vice versa.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""

from rest_framework import serializers
from .models import StixBundle

class StixBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = StixBundle
        fields = ['bundle_json']
