"""
Utility functions and classes for the STIXGen project.

This module provides helper functions and classes for generating fake data
used in STIX bundles, such as IP addresses, domain names, etc.

Author: Najmul Hasan

Copyright (c) 2023 UNCP, LAS, NSA. All rights reserved.

Contributors: []

"""

import random
import hashlib
from faker import Faker

fake = Faker()

# Class containing static methods to generate various types of cyber data
class CyberDataGenerator:
    @staticmethod
    def ip_address():
         # Generate a random IPv4 address
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    
    # Remaining methods follow a similar pattern, generating domain names, file hashes, etc.
    @staticmethod
    def domain_name():
        domains = ["com", "net", "org", "gov", "edu"]
        name = fake.word().lower()
        domain = random.choice(domains)
        return f"{name}.{domain}"

    @staticmethod
    def file_hash():
        hash_obj = hashlib.sha256(fake.word().encode())
        return hash_obj.hexdigest()

    @staticmethod
    def url():
        protocol = random.choice(["http", "https"])
        domain = CyberDataGenerator.domain_name()
        path = fake.uri_path()
        return f"{protocol}://{domain}/{path}"

    @staticmethod
    def attack_pattern_name():
        patterns = [
            "Spear Phishing", 
            "Drive-by Compromise", 
            "Exploit Public-Facing Application", 
            "SQL Injection", 
            "Cross-Site Scripting"
        ]
        return random.choice(patterns)

    
    @staticmethod
    def campaign_name():
    # These are patterns that mimic real campaign names
        prefixes = ["Operation", "Project", "Initiative", "Mission"]
        suffixes = ["Quantum", "Eagle", "Cyber", "Shadow", "Prowler"]
        descriptors = ["Silent", "Covert", "Global", "Digital", "Strategic"]
    
    # Combine randomly selected words from each list to create a campaign name
        return f"{random.choice(prefixes)} {random.choice(descriptors)} {random.choice(suffixes)}"


    @staticmethod
    def course_of_action_name():
        action_prefixes = ["Mitigate", "Prevent", "Detect", "Respond to", "Analyze"]
        action_suffixes = ["malicious activity", "network intrusions", "phishing attempts", "malware spread", "data breaches"]
        return f"{random.choice(action_prefixes)} {random.choice(action_suffixes)}"

    @staticmethod
    def course_of_action_description():
        action_descriptions = [
            "This action outlines steps to enhance security protocols and strengthen firewall configurations to thwart cyber attacks.",
            "A set of recommended practices designed to detect unauthorized access and safeguard sensitive information from exfiltration.",
            "Procedures for conducting in-depth analysis of network traffic to identify and isolate threat actors within the system.",
            "Tactics for immediate incident response upon detection of a security breach, including containment and eradication strategies.",
            "Guidelines for regular system audits to identify and remedy vulnerabilities, ensuring continuous improvement of defense mechanisms."
        ]
        return random.choice(action_descriptions)



    @staticmethod
    def grouping_name():
        themes = ["Suspicious Login Attempts", "Anomalous Data Transfers", "Irregular System Access Patterns", "Unusual IP Address Activities", "Network Scanning Anomalies"]
        return f"Grouping of {random.choice(themes)}"

    @staticmethod
    def grouping_description():
        descriptions = [
            "This grouping represents a collection of related cyber events that suggest a coordinated attempt to breach the system.",
            "A series of incidents have been grouped to analyze the pattern of external scanning activities detected across multiple endpoints.",
            "Aggregated data regarding irregular login patterns from various geo-locations to identify potential credential stuffing attacks.",
            "A set of related indicators that point towards a possible reconnaissance activity by an unknown threat actor within the network.",
            "Grouping of events that have been identified by the threat intelligence team to study the lateral movement of an intruder post-compromise."
        ]
        return random.choice(descriptions)
    

    @staticmethod
    def identity_name(role):
        first_names = ["Alex", "Jordan", "Morgan", "Casey", "Taylor"]
        last_names = ["Smith", "Johnson", "Brown", "Taylor", "Morrison"]
        return f"{random.choice(first_names)} {random.choice(last_names)}, {role}"

    @staticmethod
    def identity_role():
        roles = ["System Administrator", "Network Engineer", "Security Analyst", "Threat Researcher", "IT Auditor"]
        return random.choice(roles)
    
    @staticmethod
    def ipv4_indicator_pattern():
        ip = f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        return f"[ipv4-addr:value = '{ip}']"

    @staticmethod
    def domain_indicator_pattern():
        domain = CyberDataGenerator.domain_name()
        return f"[domain-name:value = '{domain}']"

    @staticmethod
    def file_hash_indicator_pattern():
        file_hash = CyberDataGenerator.file_hash()
        return f"[file:hashes.'SHA-256' = '{file_hash}']"

    @staticmethod
    def url_indicator_pattern():
        url = CyberDataGenerator.url()
        return f"[url:value = '{url}']"
    
    @staticmethod
    def generate_infrastructure():
        infrastructure_names = [
            "Central Command Node", "Data Processing Center", 
            "Secure Relay Server", "Threat Analysis Hub"
        ]
        infrastructure_types = [
            "command-and-control", "botnet", "hosting-malware", "exfiltration"
        ]

        name = random.choice(infrastructure_names) + " " + fake.word()
        infrastructure_type = random.choice(infrastructure_types)

        return name, infrastructure_type
    

    @staticmethod
    def generate_intrusion_set():
        intrusion_set_names = [
            "Shadow Group", "Silent Hackers", 
            "Digital Ghosts", "Cyber Syndicate"
        ]
        intrusion_set_goals = [
            "Data theft", "Espionage", 
            "Financial gain", "Disruption of services"
        ]

        name = random.choice(intrusion_set_names) + " " + fake.word()
        goal = random.choice(intrusion_set_goals)

        return name, goal
    
    
    @staticmethod
    def location_name():
        prefixes = ['North', 'South', 'East', 'West', 'Central']
        suffixes = ['ville', 'town', 'city', 'burg', 'port']
        base_name = fake.word().capitalize()
        return f"{random.choice(prefixes)} {base_name}{random.choice(suffixes)}"
    @staticmethod
    def malware_name():
        prefixes = ['Cyber', 'Dark', 'Neo', 'Quantum', 'Shadow']
        base_name = fake.word().capitalize()
        suffixes = ['Crypt', 'Blaster', 'Worm', 'Trojan', 'Ransom']
        return f"{random.choice(prefixes)}{base_name}{random.choice(suffixes)}"
    

    @staticmethod
    def malware_analysis_product():
        product_prefixes = ['CyberSecure', 'ThreatGuard', 'MalwareDetect', 'VirusScan', 'IntrusionShield']
        product_suffixes = ['Analyzer', 'Inspector', 'Scanner', 'Defender', 'Protector']
        return f"{random.choice(product_prefixes)} {random.choice(product_suffixes)}"

    @staticmethod
    def malware_analysis_results():
        result_options = [
            'No threats detected',
            'Suspicious activity observed',
            'Malware identified: ' + CyberDataGenerator.malware_name(),
            'Potential vulnerabilities found',
            'Security breach detected'
        ]
        return random.choice(result_options)
    
    @staticmethod
    def note_content():
        note_types = [
            "Intelligence Briefing: {}",
            "Threat Analysis Report: {}",
            "Security Alert: {}",
            "Incident Summary: {}",
            "Risk Assessment: {}"
        ]
        note_details = fake.sentence(nb_words=12)
        return random.choice(note_types).format(note_details)

    @staticmethod
    def author_name():
        return fake.name()
    
    @staticmethod
    def observed_data_objects():
        object_types = ['ipv4-addr', 'url', 'domain-name', 'file']
        object_details = {
            'ipv4-addr': {"type": "ipv4-addr", "value": fake.ipv4()},
            'url': {"type": "url", "value": fake.url()},
            'domain-name': {"type": "domain-name", "value": fake.domain_name()},
            'file': {"type": "file", "hashes": {"SHA-256": fake.file_hash()}}
        }
        selected_type = random.choice(object_types)
        return {selected_type: object_details[selected_type]}
    
    @staticmethod
    def report_title():
        adjectives = ["Critical", "In-depth", "Comprehensive", "Strategic", "Confidential"]
        topics = ["Cyber Threat Analysis", "Vulnerability Assessment", "Security Brief", "Intrusion Report", "Threat Landscape Overview"]
        return f"{random.choice(adjectives)} {random.choice(topics)}"

    @staticmethod
    def report_description():
        aspects = ["trends", "threat actors", "malware campaigns", "security vulnerabilities", "cybersecurity incidents"]
        actions = ["analyzed", "investigated", "summarized", "highlighted", "explored"]
        outcomes = ["key findings", "recommendations", "risk assessment", "threat mitigation strategies", "security implications"]
        return f"This report {random.choice(actions)} recent {random.choice(aspects)} and provides {random.choice(outcomes)}."
    

    @staticmethod
    def threat_actor_name():
        prefixes = ["Shadow", "Cyber", "Digital", "Phantom", "Ghost"]
        suffixes = ["Collective", "Syndicate", "Crew", "Brigade", "Network"]
        return f"{random.choice(prefixes)} {random.choice(suffixes)}"

    @staticmethod
    def threat_actor_role():
        roles = ["hacker", "espionage unit", "cybercriminal group", "information warfare team", "state-sponsored actor"]
        return random.choice(roles)
    

    @staticmethod
    def tool_name():
        tool_prefixes = ["Net", "Crypto", "Data", "Secure", "Cyber"]
        tool_suffixes = ["Scan", "Defend", "Guard", "Analyze", "Protect"]
        version = fake.bothify("v#.#.#")
        return f"{random.choice(tool_prefixes)}{random.choice(tool_suffixes)} {version}"
    
    @staticmethod
    def vulnerability_name():
        vulnerability_prefixes = ["CVE", "CAN", "VULN"]
        year = random.randint(2000, 2023)
        id_number = random.randint(1000, 9999)
        return f"{random.choice(vulnerability_prefixes)}-{year}-{id_number}"