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
The views.py file contains the controller class. It handles browser requests, retreives data, and returns a response. Currently it does this in one large method and should be broken up into smaller methods.

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
This is where all the SDO builders are kept. A builder is a class that is responsible for creating a specific SDO. The stix_bulder.py contains an abstract class that acts as an interface for all the builder classes. There are 19 builders. The incident_builder.py which creates the incident object is a stub in STIX 2.1 and will be expanded upon in future releases. Not all the builders are functional and the ones that do work are only set up to handle required properties, handling for the optional properties will need to be added. 

Functional builders, required properties only:
attack_pattern_builder.py, campaign_builder.py, course_of_action_builder.py, identity_builder.py, incident_builder.py, infrastructure_builder.py, location_builder.py, malware_builder.py, threat_actor_builder.py, tool_builder.py, vulnerability_builder.py

Non-functional builders:
grouping_builder.py, indicator_builder.py, intrusion_set_builder.py, malware_analysis_builder.py, note_builder.py, observed_data_builder.py, opinion_builder.py, report_builder.py

Several of the non-functional builders have a required property called object_refs. This property requires that these builders be given a list of created SDO ids. This means that these builders will need to be called after all the SDOs have been created. The current design does not support this and will need to be refactored.

### relationships_builder.py
This file contains the class responsible for creating SROs. There are two SRO types relationship and sighting. Currently sighting relationships are not supported and will need to be added.

### stix_builder_factory.py
This file contains the factory method that determines which builder to call based on the data it receives from the controller.

### stix_weights.py
This file contains the class that assigns the SDO weights and adjusts them accordingly.
