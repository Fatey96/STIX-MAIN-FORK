"""
URL configuration for the STIXGen application's stix_app module.

This module defines URL routes specific to the stix_app, such as for generating
STIX bundles.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""

from django.urls import path
from . import views

# URL patterns for the stix_app module
urlpatterns = [
    path('generate-bundle/', views.generate_bundle),  # Endpoint for generating STIX bundles
]
