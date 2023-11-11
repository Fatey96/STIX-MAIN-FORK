from stix2 import Relationship

class RelationshipBuilder:
    def __init__(self, source, target, relation):
        self.source = source.id
        self.target = target.id
        self.relation = relation

    def create(self):
        relationship = Relationship(relationship_type=self.relation,
                                    source_ref=self.source,
                                    target_ref=self.target)
        return relationship