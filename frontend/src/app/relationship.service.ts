import { Injectable } from '@angular/core';

// Define the type for relationships
type RelationshipMap = {
    [key: string]: {
        [relationshipType: string]: string[]
    }
}

@Injectable({
    providedIn: 'root'
})
export class RelationshipService {
    private commonRelationships = {
        "duplicate-of": ["attack-pattern", "campaign", "course-of-action", "grouping", "identity", "incident", "indicator", "infrastructure",
            "intrusion-set", "location", "malware", "malware-analysis", "note", "observed-data", "opinion", "report", "threat-actor", "tool", "vulnerability"],
        "derived-from": ["attack-pattern", "campaign", "course-of-action", "grouping", "identity", "incident", "indicator", "infrastructure",
            "intrusion-set", "location", "malware", "malware-analysis", "note", "observed-data", "opinion", "report", "threat-actor", "tool", "vulnerability"],
        "related-to": ["attack-pattern", "campaign", "course-of-action", "grouping", "identity", "incident", "indicator", "infrastructure",
            "intrusion-set", "location", "malware", "malware-analysis", "note", "observed-data", "opinion", "report", "threat-actor", "tool", "vulnerability"]
    }

    // Relationships data structure
    private relationships: RelationshipMap = {
        "attack-pattern": {
            ...this.commonRelationships,
            "delivers": ["malware"],
            "targets": ["identity", "location", "vulnerability"],
            "uses": ["malware", "tool"]
        },
        "campaign": {
            ...this.commonRelationships,
            "attributed-to": ["intrusion-set", "threat-actor"],
            "compromises": ["infrastructure"],
            "originates-from": ["location"],
            "targets": ["identity", "location", "vulnerability"],
            "uses": ["attack-pattern", "infrastructure", "malware", "tool"]
        },
        "course-of-action": {
            ...this.commonRelationships,
            "investigates": ["indicator"],
            "mitigates": ["attack-pattern", "indicator", "malware", "tool", "vulnerability"],
            "remediates": ["malware", "vulnerability"]
        },
        "grouping": {
            ...this.commonRelationships
        },
        "identity": {
            ...this.commonRelationships,
            "located-at": ["location"]
        },
        "incident": {
            ...this.commonRelationships
        },
        "indicator": {
            ...this.commonRelationships,
            "indicates": ["attack-pattern", "campaign", "infrastructure", "intrusion-set", "malware", "threat-actor", "tool"],
            "based-on": ["observed-data"]
        },
        "infrastructure": {
            ...this.commonRelationships,
            "communicates-with": ["infrastructure", "ipv4-addr", "ipv6-addr", "domain-name", "url"],
            "consists-of": ["infrastructure", "observed-data"],     // All STIX Cyber-observable Objects too, but those have not been implemented
            "controls": ["infrastructure", "malware"],
            "delivers": ["malware"],
            "has": ["vulnerability"],
            "hosts": ["tool", "malware"],
            "located-at": ["location"],
            "uses": ["infrastructure"]
        },
        "intrusion-set": {
            ...this.commonRelationships,
            "attributed-to": ["threat-actor"],
            "compromises": ["infrastructure"],
            "hosts": ["infrastructure"],
            "owns": ["infrastructure"],
            "originates-from": ["location"],
            "targets": ["identity", "location", "vulnerability"],
            "uses": ["attack-pattern", "infrastructure", "malware", "tool"]
        },
        "location": {
            ...this.commonRelationships
        },
        "malware": {
            ...this.commonRelationships,
            "authored-by": ["threat-actor", "intrusion-set"],
            "beacons-to": ["infrastructure"],
            "exfiltrates-to": ["infrastructure"],
            "communicates-with": ["ipv4-addr", "ipv6-addr", "domain-name", "url"],
            "controls": ["malware"],
            "downloads": ["malware", "tool", "file"],
            "drops": ["malware", "tool", "file"],
            "exploits": ["vulnerability"],
            "originates-from": ["location"],
            "targets": ["identity", "infrastructure", "location", "vulnerability"],
            "uses": ["attack-pattern", "infrastructure", "malware", "tool"],
            "variant-of": ["malware"]
        },
        "malware-analysis": {
            ...this.commonRelationships,
            "characterizes": ["malware"],
            "analysis-of": ["malware"],
            "static-analysis-of": ["malware"],
            "dynamic-analysis-of": ["malware"]
        },
        "note": {
            ...this.commonRelationships     // Need to look more into the relationships for this.
        },
        "observed-data": {
            ...this.commonRelationships
        },
        "opinion": {
            ...this.commonRelationships
        },
        "report": {
            ...this.commonRelationships
        },
        "threat-actor": {
            ...this.commonRelationships,
            "attributed-to": ["identity"],
            "compromises": ["infrastructure"],
            "hosts": ["infrastructure"],
            "owns": ["infrastructure"],
            "impersonates": ["identity"],
            "located-at": ["location"],
            "targets": ["identity", "location", "vulnerability"],
            "uses": ["attack-pattern", "infrastructure", "malware", "tool"]
        },
        "tool": {
            ...this.commonRelationships,
            "delivers": ["malware"],
            "drops": ["malware"],
            "has": ["vulnerability"],
            "targets": ["identity", "infrastructure", "location", "vulnerability"],
            "uses": ["infrastructure"]
        },
        "vulnerability": {
            ...this.commonRelationships
        }
    }

    // Fetches the possible relationships between a source and a target STIX type
    getPossibleRelationships(sourceType: string, targetType: string): string[] {
        const sourceRelationships = this.relationships[sourceType]
        if (!sourceRelationships) {
            return []
        }

        // Find relationship types where the target is allowed
        return Object.keys(sourceRelationships).filter(relationshipType => sourceRelationships[relationshipType].includes(targetType))
    }
}
