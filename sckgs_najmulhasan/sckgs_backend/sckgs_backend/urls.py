"""
URL configuration for the sckgs_backend project.

This module defines the URL routes for the STIXGen application. It includes routes
to various app modules and the admin interface.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""
# Import necessary Django modules for URL configuration
from django.contrib import admin
from django.urls import include, path

# URL patterns defining the routing of requests to respective views
urlpatterns = [
    path('admin/', admin.site.urls), # Admin site URLs
    path('api/', include('stix_app.urls')), # Include URLs from the stix_app application
]
