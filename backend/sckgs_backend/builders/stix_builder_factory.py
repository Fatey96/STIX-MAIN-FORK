from .identity_builder import IdentityBuilder
from .threat_actor_builder import ThreatActorBuilder
from .malware_builder import MalwareBuilder
from .campaign_builder import CampaignBuilder
from .location_builder import LocationBuilder

class StixBuilderFactory:
    @staticmethod
    def create(type, name):
        match type:
            case "identity":
                return IdentityBuilder(name).create()
            case "threat-actor":
                return ThreatActorBuilder(name).create()
            case "malware":
                return MalwareBuilder(name).create()
            case "campaign":
                return CampaignBuilder(name).create()
            case "location":
                return LocationBuilder(name).create()
            case _:
                print("Done")