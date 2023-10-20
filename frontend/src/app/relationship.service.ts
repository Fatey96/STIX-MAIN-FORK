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
    "identity": {
        ...this.commonRelationships,
        "located-at": ["location"]
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
