from identity_builder import IdentityBuilder
class StixBuilderFactory:
    @classmethod
    def create(stix_type, name):
        match stix_type:
            case (stix_type, "identity"):
                IdentityBuilder.create(name)
            case _:
                raise ValueError("Not a STIX type")