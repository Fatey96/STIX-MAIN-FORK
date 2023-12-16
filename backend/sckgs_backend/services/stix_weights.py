
class StixWeights:
    @staticmethod
    def get_weights(stix_objects):
        weights = {          
            'attack-pattern': 0.05,
            'campaign': 0.05,
            'course-of-action': 0.05,
            'grouping': 0.10,
            'identity': 0.20,
            'incident': 0.10,
            'indicator': 0.10,
            'infrastructure': 0.10,
            'intrusion-set': 0.10,
            'location': 0.10,
            'malware': 0.10,
            'malware-analysis': 0.10,
            'note': 0.10,
            'observed-data': 0.10,
            'opinion': 0.10,
            'report': 0.10,
            'threat-actor':  0.15,
            'tool': 0.10,
            'vulnerability': 0.10
        }

        stix_weights = {}
        for stix in (stix_objects):
            weight = weights.get(stix['type'])
            stix_weights[stix_objects.index(stix)] = weight

        return stix_weights
    
    @staticmethod
    def adjust_weights(weights):
        current_sum = sum(weights.values())

        if current_sum < 1:
            difference = 1 - current_sum
            adjustment = difference / len(weights)
            adjusted_dict = {key: value + adjustment for key, value in weights.items()}
        elif current_sum > 1:
            difference = current_sum - 1
            adjustment = difference / len(weights)
            adjusted_dict = {key: value - adjustment for key, value in weights.items()}
        else:
            return weights
        
        return adjusted_dict