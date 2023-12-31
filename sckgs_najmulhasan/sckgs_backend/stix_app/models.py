"""
Models for the STIXGen project.

This module defines the data models, particularly for storing STIX bundles.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""

from django.db import models

# Definition of StixBundle model for storing STIX bundles in the database
class StixBundle(models.Model):
    bundle_json = models.TextField()  # Field to store JSON string of STIX bundle
    created_at = models.DateTimeField(auto_now_add=True) # Timestamp for bundle creation

    def __str__(self):
        return f"STIX Bundle {self.id}" # Human-readable representation of the model
