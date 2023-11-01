from .identity_builder import IdentityBuilder
from .threat_actor_builder import ThreatActorBuilder

class StixBuilderFactory:
    @staticmethod
    def create(type, name):
        match type:
            case "identity":
                return IdentityBuilder(name).create()
            case "threat-actor":
                return ThreatActorBuilder(name).create()
            case _:
                print("Done")