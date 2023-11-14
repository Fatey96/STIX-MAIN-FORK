
class StixProportions:
    @staticmethod
    def get_proportions(type):
        match type:
            case 'attack-pattern':
                return 
            case 'campaign':
                return 0.10
            case 'course-of-action':
                return 
            case 'grouping':
                return 
            case 'identity':
                return 0.25
            case 'incident':
                return 
            case 'indicator':
                return 
            case 'infrastructure':
                return 
            case 'intrusion-set':
                return 
            case 'location':
                return 0.15
            case 'malware': 
                return 0.15
            case 'malware-analysis':
                return 
            case 'note':
                return 
            case 'observed-data':
                return 
            case 'opinion':
                return 
            case 'report':
                return 
            case 'threat-actor':
                return 0.10
            case 'tool':
                return 
            case 'vulnerability':
                return 
            case _:
                print("No match found")
    
    @staticmethod
    def adjust_proportions(proportions):
        current_sum = sum(proportions.values())

        if current_sum < 1:
            difference = 1 - current_sum
            adjustment = difference / len(proportions)
            adjusted_dict = {key: value + adjustment for key, value in proportions.items()}
        elif current_sum > 1:
            difference = current_sum - 1
            adjustment = difference / len(proportions)
            adjusted_dict = {key: value - adjustment for key, value in proportions.items()}
        else:
            return proportions
        
        return adjusted_dict