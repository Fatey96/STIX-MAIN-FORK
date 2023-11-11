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
                return attack_pattern_builder.AttackPatternBuilder(stix['object']).create()
            case 'campaign':
                return campaign_builder.CampaignBuilder(stix['object']).create()
            case 'course-of-action':
                return course_of_action_builder.CourseOfActionBuilder(stix['object']).create()
            case 'grouping':
                return grouping_builder.GroupingBuilder(stix['object']).create()
            case 'identity':
                return identity_builder.IdentityBuilder(stix['object']).create()
            case 'incident':
                return incident_builder.IncidentBuilder(stix['object']).create()
            case 'indicator':
                return indicator_builder.IndicatorBuilder(stix['object']).create()
            case 'infrastructure':
                return infrastructure_builder.InfrastructureBuilder(stix['object']).create()
            case 'intrusion-set':
                return intrusion_set_builder.IntrusionSetBuilder(stix['object']).create()
            case 'location':
                return location_builder.LocationBuilder(stix['object']).create()
            case 'malware':
                return malware_builder.MalwareBuilder(stix['object']).create()
            case 'malware-analysis':
                return malware_analysis_builder.MalwareAnalysisBuilder(stix['object']).create()
            case 'note':
                return note_builder.NoteBuilder(stix['object']).create()
            case 'observed-data':
                return observed_data_builder.ObservedDataBuilder(stix['object']).create()
            case 'opinion':
                return opinion_builder.OpinionBuilder(stix['object']).create()
            case 'report':
                return report_builder.ReportBuilder(stix['object']).create()
            case 'threat-actor':
                return threat_actor_builder.ThreatActorBuilder(stix['object']).create()
            case 'tool':
                return tool_builder.ToolBuilder(stix['object']).create()
            case 'vulnerability':
                return vulnerability_builder.VulnerabilityBuilder(stix['object']).create()
            case _:
                print("No match found")