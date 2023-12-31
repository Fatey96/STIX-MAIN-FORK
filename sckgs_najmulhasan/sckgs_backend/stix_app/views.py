"""
Views for the STIXGen application's stix_app module.

This module contains view functions for handling requests related to STIX
bundle generation and manipulation.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""

from stix2 import (ThreatActor, Malware, Identity, Relationship, Bundle, 
                   AttackPattern, Campaign, CourseOfAction, Grouping, Indicator, 
                   Infrastructure, IntrusionSet, Location, MalwareAnalysis, Note,
                   ObservedData, Opinion, Report, Tool, Vulnerability, Bundle)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from faker import Faker
from .utils import CyberDataGenerator
from .models import StixBundle
import random


fake = Faker()

cyber_data_gen = CyberDataGenerator()

def get_stix_id(entity_type):
      # Generate a unique STIX ID for a given entity type
    return f"{entity_type}--{fake.uuid4()}"

@api_view(['POST'])
def generate_bundle(request):
      # Extract STIX object types selected for bundle generation from the request
    attack_pattern_selected = request.data.get('attackPattern', False)
    campaign_selected = request.data.get('campaign', False)
    course_of_action_selected = request.data.get('courseOfAction', False)
    grouping_selected = request.data.get('grouping', False)
    identity_selected = request.data.get('identity', False)
    indicator_selected = request.data.get('indicator', False)
    infrastructure_selected = request.data.get('infrastructure', False)   
    intrusion_set_selected = request.data.get('intrusionSet', False)
    location_selected = request.data.get('location', False)
    malware_selected = request.data.get('malware', False)
    malware_analysis_selected = request.data.get('malwareAnalysis', False)
    note_selected = request.data.get('note', False)
    observed_data_selected = request.data.get('observedData', False)
    opinion_selected = request.data.get('opinion', False)
    report_selected = request.data.get('report', False)
    threat_actor_selected = request.data.get('threatActor', False)
    tool_selected = request.data.get('tool', False)
    vulnerability_selected = request.data.get('vulnerability', False)
    
  
    stix_objects = {}
    
    # Conditional logic for creating STIX objects based on selections
    if attack_pattern_selected:
        # Create an AttackPattern object if selected
        attack_pattern = AttackPattern(
            type='attack-pattern', 
            id=get_stix_id('attack-pattern'), 
            name= cyber_data_gen.attack_pattern_name()
        )
        stix_objects['attack_pattern'] = attack_pattern
    
     # More conditional logic for other STIX objects like Campaign, Malware, etc.
    if campaign_selected:
        campaign = Campaign(
            type='campaign', 
            id=get_stix_id('campaign'), 
            name=cyber_data_gen.campaign_name()
        )
        stix_objects['campaign'] = campaign
    
    if course_of_action_selected:
        course_of_action = CourseOfAction(
            type='course-of-action', 
            id=get_stix_id('course-of-action'), 
            name=cyber_data_gen.course_of_action_name(),
            description=cyber_data_gen.course_of_action_description()
        )
        stix_objects['course_of_action'] = course_of_action

    if grouping_selected:
        grouping = Grouping(
            type='grouping', 
            id=get_stix_id('grouping'), 
            name=cyber_data_gen.grouping_name(),
            description=cyber_data_gen.grouping_description(), 
            context='suspicious-activity'
        )
        stix_objects['grouping'] = grouping
    
    if identity_selected:
        role = cyber_data_gen.identity_role()
        identity = Identity(
            type='identity',
            id=get_stix_id('identity'),
            name=cyber_data_gen.identity_name(role),
            identity_class='individual',
            roles=[role],  
            sectors=["technology", "financial", "government"]  
        )
        stix_objects['identity'] = identity

    if indicator_selected:
        indicator_patterns = [
            cyber_data_gen.ipv4_indicator_pattern(),
            cyber_data_gen.domain_indicator_pattern(),
            cyber_data_gen.file_hash_indicator_pattern(),
            cyber_data_gen.url_indicator_pattern()
        ]
        pattern = random.choice(indicator_patterns)
        indicator = Indicator(
            type='indicator',
            id=get_stix_id('indicator'),
            name="Suspicious Cyber Activity Indicator",
            pattern=pattern,
            pattern_type="stix"
        )
        stix_objects['indicator'] = indicator


    if infrastructure_selected:
        infra_name, infra_type = cyber_data_gen.generate_infrastructure()

        infrastructure = Infrastructure(
            type='infrastructure', 
            id=get_stix_id('infrastructure'), 
            name=infra_name, 
            infrastructure_types=[infra_type]
        )
        stix_objects['infrastructure'] = infrastructure


    if intrusion_set_selected:
        intrusion_set_name, intrusion_set_goal = cyber_data_gen.generate_intrusion_set()
        intrusion_set = IntrusionSet(
            type='intrusion-set', 
            id=get_stix_id('intrusion-set'), 
            name=intrusion_set_name, 
            goals=[intrusion_set_goal]
        )
        stix_objects['intrusion_set'] = intrusion_set


    if location_selected:
        location_name = cyber_data_gen.location_name()
        latitude = fake.latitude()
        longitude = fake.longitude()
        location = Location(
            type='location',
            id=get_stix_id('location'),
            name=location_name,
            latitude=latitude,
            longitude=longitude
        )
        stix_objects['location'] = location


    if malware_selected:
        malware_name = cyber_data_gen.malware_name()
        malware_types = ['ransomware']  # or any other type, possibly randomly selected
        malware = Malware(
            type='malware',
            id=get_stix_id('malware'),
            name=malware_name,
            malware_types=malware_types,
            is_family=False
        )
        stix_objects['malware'] = malware


    if malware_analysis_selected:
        product_name = cyber_data_gen.malware_analysis_product()
        analysis_results = cyber_data_gen.malware_analysis_results()
        malware_analysis = MalwareAnalysis(
            type='malware-analysis',
            id=get_stix_id('malware-analysis'),
            product=product_name,
            version=fake.bothify('v#.#.#'),  
            results=analysis_results
        )
        stix_objects['malware_analysis'] = malware_analysis


    if note_selected:
        note_content = cyber_data_gen.note_content()
        author_name = cyber_data_gen.author_name()
        note = Note(
            type='note',
            id=get_stix_id('note'),
            content=note_content,
            authors=[author_name]
        )
        stix_objects['note'] = note


    if observed_data_selected:
        observed_objects = cyber_data_gen.observed_data_objects()
        observed_data = ObservedData(
            type='observed-data',
            id=get_stix_id('observed-data'),
            first_observed=fake.iso8601(),
            last_observed=fake.iso8601(),
            number_observed=1,
            objects=observed_objects
        )
        stix_objects['observed_data'] = observed_data


    if opinion_selected:
        opinion = Opinion(
            type='opinion', 
            id=get_stix_id('opinion'), 
            explanation=fake.sentence(),
            authors=[fake.name()],
            opinion="agree"
        )
        stix_objects['opinion'] = opinion

    if report_selected:
        report_title = cyber_data_gen.report_title()
        report_description = cyber_data_gen.report_description()
        report = Report(
            type='report',
            id=get_stix_id('report'),
            name=report_title,
            description=report_description,
            published=fake.iso8601(),
            report_types=['campaign'],
            object_refs=[]
        )
        stix_objects['report'] = report

    
    if threat_actor_selected:
        threat_actor_name = cyber_data_gen.threat_actor_name()
        threat_actor_role = cyber_data_gen.threat_actor_role()
        threat_actor = ThreatActor(
            type='threat-actor',
            id=get_stix_id('threat-actor'),
            name=threat_actor_name,
            roles=[threat_actor_role]
        )
        stix_objects['threat_actor'] = threat_actor


    if tool_selected:
        tool_name = cyber_data_gen.tool_name()
        tool = Tool(
            type='tool', 
            id=get_stix_id('tool'), 
            name=tool_name,
            tool_version="1.0" 
        )
        stix_objects['tool'] = tool


    if vulnerability_selected:
        vulnerability_name = cyber_data_gen.vulnerability_name()
        vulnerability = Vulnerability(
            type='vulnerability', 
            id=get_stix_id('vulnerability'), 
            name=vulnerability_name
        )
        stix_objects['vulnerability'] = vulnerability


    # Creating relationships between different STIX objects if applicable
    # Example: if 'threat_actor' in stix_objects and 'attack_pattern' in stix_objects:
    relationship_objects = []
    if 'threat_actor' in stix_objects and 'attack_pattern' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='uses',
            source_ref=stix_objects['threat_actor'].id,
            target_ref=stix_objects['attack_pattern'].id,
            description=f"{stix_objects['threat_actor'].name} uses {stix_objects['attack_pattern'].name}"
        )
        relationship_objects.append(relationship)

    # Attack Pattern and Malware:
    if 'attack_pattern' in stix_objects and 'malware' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='uses',
            source_ref=stix_objects['malware'].id,
            target_ref=stix_objects['attack_pattern'].id,
            description=f"{stix_objects['malware'].name} uses {stix_objects['attack_pattern'].name}"
        )
        relationship_objects.append(relationship)


    # Campaign and Attack Pattern:
    if 'campaign' in stix_objects and 'attack_pattern' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='uses',
            source_ref=stix_objects['campaign'].id,
            target_ref=stix_objects['attack_pattern'].id,
            description=f"{stix_objects['campaign'].name} uses {stix_objects['attack_pattern'].name}"
        )
        relationship_objects.append(relationship)

    # Campaign and Threat Actor:
    if 'campaign' in stix_objects and 'threat_actor' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='attributed-to',
            source_ref=stix_objects['campaign'].id,
            target_ref=stix_objects['threat_actor'].id,
            description=f"{stix_objects['campaign'].name} attributed to {stix_objects['threat_actor'].name}"
        )
        relationship_objects.append(relationship)
    
     # Relating a Course of Action to a Threat Actor (mitigates relationship)
    if 'course_of_action' in stix_objects and 'threat_actor' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='mitigates',
            source_ref=stix_objects['course_of_action'].id,
            target_ref=stix_objects['threat_actor'].id,
            description=f"{stix_objects['course_of_action'].name} mitigates the threat of {stix_objects['threat_actor'].name}"
        )
        relationship_objects.append(relationship)

    # Grouping related to an Identity (sighting relationship)
    if 'grouping' in stix_objects and 'identity' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='sighting',
            source_ref=stix_objects['grouping'].id,
            target_ref=stix_objects['identity'].id,
            description=f"{stix_objects['grouping'].name} sighting related to {stix_objects['identity'].name}"
        )
        relationship_objects.append(relationship)
     
     # Indicator related to Malware (indicates relationship)
    if 'indicator' in stix_objects and 'malware' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='indicates',
            source_ref=stix_objects['indicator'].id,
            target_ref=stix_objects['malware'].id,
            description=f"{stix_objects['indicator'].name} indicates {stix_objects['malware'].name}"
        )
        relationship_objects.append(relationship)
      

    # Indicator and Threat Actor:
    if 'indicator' in stix_objects and 'threat_actor' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='indicates',
            source_ref=stix_objects['indicator'].id,
            target_ref=stix_objects['threat_actor'].id,
            description=f"{stix_objects['indicator'].name} indicates activity of {stix_objects['threat_actor'].name}"
        )
        relationship_objects.append(relationship)
  
    # Infrastructure and Campaign:
    if 'infrastructure' in stix_objects and 'campaign' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='compromises',
            source_ref=stix_objects['campaign'].id,
            target_ref=stix_objects['infrastructure'].id,
            description=f"{stix_objects['campaign'].name} compromises {stix_objects['infrastructure'].name}"
        )
        relationship_objects.append(relationship)

    # Infrastructure related to Threat Actor (used-by relationship)
    if 'infrastructure' in stix_objects and 'threat_actor' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='used-by',
            source_ref=stix_objects['infrastructure'].id,
            target_ref=stix_objects['threat_actor'].id,
            description=f"{stix_objects['infrastructure'].name} used by {stix_objects['threat_actor'].name}"
        )
        relationship_objects.append(relationship)

    # Intrusion Set related to Threat Actor (attributed-to relationship)
    if 'intrusion_set' in stix_objects and 'threat_actor' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='attributed-to',
            source_ref=stix_objects['intrusion_set'].id,
            target_ref=stix_objects['threat_actor'].id,
            description=f"{stix_objects['intrusion_set'].name} attributed to {stix_objects['threat_actor'].name}"
        )
        relationship_objects.append(relationship)

    # Location related to Infrastructure (located-at relationship)
    if 'location' in stix_objects and 'infrastructure' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='located-at',
            source_ref=stix_objects['location'].id,
            target_ref=stix_objects['infrastructure'].id,
            description=f"{stix_objects['location'].name} located at {stix_objects['infrastructure'].name}"
        )
        relationship_objects.append(relationship)

    # Malware and Identity
    if 'malware' in stix_objects and 'identity' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='targets',
            source_ref=stix_objects['malware'].id,
            target_ref=stix_objects['identity'].id,
            description=f"{stix_objects['malware'].name} targets {stix_objects['identity'].name}"
        )
        relationship_objects.append(relationship)


    
    # Malware Analysis related to Malware (analysis-of relationship)
    if 'malware_analysis' in stix_objects and 'malware' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='analysis-of',
            source_ref=stix_objects['malware_analysis'].id,
            target_ref=stix_objects['malware'].id,
            description=f"{stix_objects['malware_analysis'].product} analysis of {stix_objects['malware'].name}"
        )
        relationship_objects.append(relationship)

    # Note related to Campaign (information-about relationship)
    if 'note' in stix_objects and 'campaign' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='information-about',
            source_ref=stix_objects['note'].id,
            target_ref=stix_objects['campaign'].id,
            description=f"Note about {stix_objects['campaign'].name}"
        )
        relationship_objects.append(relationship)

     # Opinion related to Report (opinion-on relationship)
    if 'opinion' in stix_objects and 'report' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='opinion-on',
            source_ref=stix_objects['opinion'].id,
            target_ref=stix_objects['report'].id,
            description=f"Opinion by {', '.join(stix_objects['opinion'].authors)} on {stix_objects['report'].name}"
        )
        relationship_objects.append(relationship)

    # Observed Data related to Indicator (indicates relationship)
    if 'observed_data' in stix_objects and 'indicator' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='indicates',
            source_ref=stix_objects['observed_data'].id,
            target_ref=stix_objects['indicator'].id,
            description=f"Observed data indicates {stix_objects['indicator'].name}"
        )
        relationship_objects.append(relationship)

    # Observed Data and Campaign:
    if 'observed_data' in stix_objects and 'campaign' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='related-to',
            source_ref=stix_objects['observed_data'].id,
            target_ref=stix_objects['campaign'].id,
            description=f"Observed data related to {stix_objects['campaign'].name}"
        )
        relationship_objects.append(relationship)



     # Report related to Threat Actor (sighting-of relationship)
    if 'report' in stix_objects and 'threat_actor' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='sighting-of',
            source_ref=stix_objects['report'].id,
            target_ref=stix_objects['threat_actor'].id,
            description=f"Report {stix_objects['report'].name} includes sighting of {stix_objects['threat_actor'].name}"
        )
        relationship_objects.append(relationship)

    # Threat Actor and Malware
    if 'threat_actor' in stix_objects and 'malware' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='uses',
            source_ref=stix_objects['threat_actor'].id,
            target_ref=stix_objects['malware'].id,
            description=f"{stix_objects['threat_actor'].name} uses {stix_objects['malware'].name}"
        )
        relationship_objects.append(relationship)
        
      # Tool used to exploit a Vulnerability
    if 'tool' in stix_objects and 'vulnerability' in stix_objects:
        relationship = Relationship(
            type='relationship',
            relationship_type='uses',
            source_ref=stix_objects['tool'].id,
            target_ref=stix_objects['vulnerability'].id,
            description=f"{stix_objects['tool'].name} uses {stix_objects['vulnerability'].name}"
        )
        relationship_objects.append(relationship)

  
    # Bundle all STIX objects and relationships together
    bundle = Bundle(objects=list(stix_objects.values()) + relationship_objects)
    serialized_bundle = bundle.serialize(pretty=True)

    # Save the bundle to the database
    stix_bundle = StixBundle(bundle_json=serialized_bundle)
    stix_bundle.save()
    
    # Respond with the serialized bundle
    return Response({"bundle_json": serialized_bundle})

