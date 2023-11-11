from stix_builders import (attack_pattern_builder, campaign_builder, course_of_action_builder,
    grouping_builder, identity_builder, incident_builder, indicator_builder, infrastructure_builder,
    intrusion_set_builder, location_builder, malware_builder, malware_analysis_builder, note_builder,
    observed_data_builder, opinion_builder, report_builder, threat_actor_builder, tool_builder,
    vulnerability_builder)

class StixBuilderFactory:
    @staticmethod
    def create(stix):
        match stix['type']:
            case 'attack-pattern':
                # required: name
                return attack_pattern_builder.AttackPatternBuilder()
            case 'campaign':
                # required: name
                return campaign_builder.CampaignBuilder()
            case 'course-of-action':
                # required: name
                return course_of_action_builder.CourseOfActionBuilder()
            case 'grouping':
                # required: context, object_refs
                return grouping_builder.GroupingBuilder()
            case 'identity':
                return identity_builder.IdentityBuilder(stix['name'], stix['identity_class'], stix['options']).create()
            case 'incident':
                # required: name
                return incident_builder.IncidentBuilder()
            case 'indicator':
                # required: pattern, pattern_type, valid_from
                return indicator_builder.IndicatorBuilder()
            case 'infrastructure':
                # required: name
                return infrastructure_builder.InfrastructureBuilder()
            case 'intrusion-set':
                # required: name
                return intrusion_set_builder.IntrusionSetBuilder()
            case 'location':
                # Must be provided at least one: region, country, latitude and longitude
                return location_builder.LocationBuilder(stix['name']).create()
            case 'malware':
                return malware_builder.MalwareBuilder(stix['is-family'], stix['options']).create()
            case 'malware-analysis':
                # required: product
                return malware_analysis_builder.MalwareAnalysisBuilder()
            case 'note':
                # required: content, object_refs
                return note_builder.NoteBuilder()
            case 'observed-data':
                # required: first_observed, last_observed, number_observed
                return observed_data_builder.ObservedDataBuilder()
            case 'opinion':
                # required: opinion, object_refs
                return opinion_builder.OpinionBuilder()
            case 'report':
                # required: name, published, object_refs
                return report_builder.ReportBuilder()
            case 'threat-actor':
                return threat_actor_builder.ThreatActorBuilder(stix['name'], stix['options']).create()
            case 'tool':
                # required: name
                return tool_builder.ToolBuilder()
            case 'vulnerability':
                # required: name
                return vulnerability_builder.VulnerabilityBuilder()
            case _:
                print("No match found")