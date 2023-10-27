from .identity_builder import IdentityBuilder
from .threat_actor_builder import ThreatActorBuilder

class StixBuilderFactory:
    @staticmethod
    def create(type, name):
        match type:
            case "identity":
                print(IdentityBuilder(name).create().serialize(pretty=True))
            case "threat-actor":
                print(ThreatActorBuilder(name).create().serialize(pretty=True))
            case _:
                print("Done")