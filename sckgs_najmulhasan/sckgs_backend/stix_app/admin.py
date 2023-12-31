"""
Django admin configuration for the STIXGen project.

This module registers models with the Django admin interface, enabling
administration of the STIX bundles.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""
from django.contrib import admin
from .models import StixBundle

# Registering the StixBundle model with the Django admin site for easy administration
admin.site.register(StixBundle)
