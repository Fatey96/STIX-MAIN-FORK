from stix2 import Relationship

class RelationshipBuilder:
    def __init__(self, source, target, relationship):
        self.source = source
        self.target = target
        self.relationship = relationship

    def create(self):
        relationship = Relationship(relationship_type=self.relationship,
                                    source_ref=self.source.id,
                                    target_ref=self.target.id)
        return relationship