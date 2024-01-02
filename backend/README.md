# Backend Breakdown

## api folder
```bash
 api
  ┣ migrations
  ┣ admin.py
  ┣ apps.py
  ┣ models.py
  ┣ tests.py
  ┣ urls.py
  ┣ views.py
  ┗ __init__.py
```
 ### test.py
This is where tests are written. Currently there is one test , test_json_data, that generates a small SKG using mock data. Tests can be run by navigating to the backend folder and entering the following command in the console:
```bash
 py manage.py test
```
 ### views.py
The views.py file acts as the controller class. It handles browser request, retreives data, and returns a response. Currently it does this in one large method and should be broken up into smaller methods.

 ## services folder
 ```bash
  services
  ┣ stix_builders
  ┃ ┣ attack_pattern_builder.py
  ┃ ┣ campaign_builder.py
  ┃ ┣ course_of_action_builder.py
  ┃ ┣ grouping_builder.py
  ┃ ┣ identity_builder.py
  ┃ ┣ incident_builder.py
  ┃ ┣ indicator_builder.py
  ┃ ┣ infrastructure_builder.py
  ┃ ┣ intrusion_set_builder.py
  ┃ ┣ location_builder.py
  ┃ ┣ malware_analysis_builder.py
  ┃ ┣ malware_builder.py
  ┃ ┣ note_builder.py
  ┃ ┣ observed_data_builder.py
  ┃ ┣ opinion_builder.py
  ┃ ┣ report_builder.py
  ┃ ┣ stix_builder.py
  ┃ ┣ threat_actor_builder.py
  ┃ ┣ tool_builder.py
  ┃ ┣ vulnerability_builder.py
  ┃ ┗ __init__.py
  ┣ relationship_builder.py
  ┣ stix_builder_factory.py
  ┣ stix_weights.py
  ┗ __init__.py
```

 ### stix_builders folder

 ### relationships_builder.py

 ### stix_builder_factory.py
 
 ### stix_weights.py
 
