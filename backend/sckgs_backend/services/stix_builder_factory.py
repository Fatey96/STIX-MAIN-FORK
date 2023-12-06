from .stix_builders import (attack_pattern_builder, campaign_builder, course_of_action_builder,
    grouping_builder, identity_builder, incident_builder, indicator_builder, infrastructure_builder,
    intrusion_set_builder, location_builder, malware_builder, malware_analysis_builder, note_builder,
    observed_data_builder, opinion_builder, report_builder, threat_actor_builder, tool_builder,
    vulnerability_builder)

class StixBuilderFactory:
    @staticmethod
    def create(stix):
        match stix['type']:
            case 'attack-pattern':
                return attack_pattern_builder.AttackPatternBuilder(stix).create()
            case 'campaign':
                return campaign_builder.CampaignBuilder(stix).create()
            case 'course-of-action':
                return course_of_action_builder.CourseOfActionBuilder(stix).create()
            case 'grouping':
                return grouping_builder.GroupingBuilder(stix).create()
            case 'identity':
                return identity_builder.IdentityBuilder(stix).create()
            case 'incident':
                return incident_builder.IncidentBuilder(stix).create()
            case 'indicator':
                return indicator_builder.IndicatorBuilder(stix).create()
            case 'infrastructure':
                return infrastructure_builder.InfrastructureBuilder(stix).create()
            case 'intrusion-set':
                return intrusion_set_builder.IntrusionSetBuilder(stix).create()
            case 'location':
                return location_builder.LocationBuilder(stix).create()
            case 'malware':
                return malware_builder.MalwareBuilder(stix).create()
            case 'malware-analysis':
                return malware_analysis_builder.MalwareAnalysisBuilder(stix).create()
            case 'note':
                return note_builder.NoteBuilder(stix).create()
            case 'observed-data':
                return observed_data_builder.ObservedDataBuilder(stix).create()
            case 'opinion':
                return opinion_builder.OpinionBuilder(stix).create()
            case 'report':
                return report_builder.ReportBuilder(stix).create()
            case 'threat-actor':
                return threat_actor_builder.ThreatActorBuilder(stix).create()
            case 'tool':
                return tool_builder.ToolBuilder(stix).create()
            case 'vulnerability':
                return vulnerability_builder.VulnerabilityBuilder(stix).create()
            case _:
                print("No match found")