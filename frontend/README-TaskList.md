# Frontend Branch Task List

This is to provide a status update of the objects and other features. 

### Miscellaneous

This section will compose of tasks that need to be completed, but do not fit within another category.

- Timestamps are possibly not set up to be in the correct format for STIX 2.1.

### STIX Domain Objects (SDOs)

There are 19 total SDOs, and those are primarily what have been worked on through Fall 2023. Below lists the tasks that are still needed for each object. For more documentation on SDOs, please visit [Section 4 in the STIX 2.1 documentation](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_nrhq5e9nylke).

1. [**Attack Pattern**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_axjijf603msy)
    - Needs property `kill_chain_phases` **(optional)* → type *list of type kill-chain-phase*

2. [**Campaign**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_pcpvfz4ik6d6)
    - If `first_seen` and `last_seen` are both defined, `last_seen` must be greater than or equal to `first_seen`

3. [**Course of Action**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a925mpw39txn)
    - Needs property `action` *(reserved)* → type *RESERVED*

4. [**Grouping**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_t56pn7elv6u7)
    - Needs property `object_refs` *(required)* → type *list of type identifier*

5. [**Identity**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp)
    - Finish property `sectors` *(optional)* → type *list of type open-vocab*
        - All open-vocab fields are not available as options in the HTML currently
        - Options should come from the `industry-sector-ov` open vocabulary

6. [**Incident**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_sczfhw64pjxt)
    - This one should be complete.

7. [**Indicator**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_muftrcpnf89v)
    - If `valid_until` is defined, `valid_until` must be greater than `valid_from`
    - Needs property `kill_chain_phases` *(optional)* → type *list of type kill-chain-phase*

8. [**Infrastructure**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_jo3k1o6lr9)
    - Needs property `kill_chain_phases` *(optional)* → type *list of type kill-chain-phase*
    - If `first_seen` and `last_seen` are both defined, `last_seen` must be greater than or equal to `first_seen`

9. [**Intrusion Set**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_5ol9xlbbnrdn)
    - If `first_seen` and `last_seen` are both defined, `last_seen` must be greater than or equal to `first_seen`

10. [**Location**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_th8nitr8jb4k)
    - Need to ensure that either `region`, `country`, or both `latitude` and `longitude` are defined before it is marked a valid form
        - These properties are optional by default, but at least one of these properties/sets of properties are required 
    - If `latitude` is defined, `longitude` must also be defined
    - If `precision` is defined, both `latitude` and `longitude` must also be defined
    - Finish property `region` *(required)* → type *open-vocab*
        - All open-vocab fields are not available as options in the HTML currently
        - Options should come from the `region-ov` open vocabulary

11. [**Malware**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_s5l7katgbp09)
    - Finish property `malware_types` *(required)* → type *list of type open-vocab*
        - All open-vocab fields are not available as options in the HTML currently
        - Options should come from the `malware-type-ov` open vocabulary
    - Needs property `kill_chain_phases` *(optional)* → type *list of type kill-chain-phase*
    - If `first_seen` and `last_seen` are both defined, `last_seen` must be greater than or equal to `first_seen`
    - Needs property `operating_system_refs` *(optional)* → type *list of type identifier*
    - Finish property `capabilities` *(optional)* → type *list of type open-vocab*
        - All open-vocab fields are not available as options in the HTML currently
        - Options should come from the `malware-capabilities-ov` open vocabulary
    - Needs property `sample_refs` *(optional)* → type *list of type identifier*

12. [**Malware Analysis**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_6hdrixb3ua4j)
    - If the name of a `product` cannot be specified, a value of "anonymized" must be used
        - This is a required field and it currently does not allow the user to proceed if it is not complete
    - Needs property `host_vm_ref` *(optional)* → type *identifier*
    - Needs property `operating_system_ref` *(optional)* → type *identifier*
    - Needs property `installed_software_refs` *(optional)* → type *list of type identifier*
    - Needs property `analysis_sco_refs` *(optional)* → type *list of type identifier*
    - Needs property `sample_ref` *(optional)* → type *identifier*

13. [**Note**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_gudodcg1sbb9)
    - Needs property `object_refs` *(required)* → type *list of type identifier*

14. [**Observed Data**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_p49j1fwoxldc)
    - Property `last_observed` must be greater than or equal to `first_observed`
    - Property `objects` is deprecated in favor of property `object_refs` and will be removed in a future version
    - Needs property `object_refs` *(optional)* → type *list of type identifier*

15. [**Opinion**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_ht1vtzfbtzda)
    - Needs property `object_refs` *(required)* → type *list of type identifier*

16. [**Report**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_n8bjzg1ysgdq)
    - Needs property `object_refs` *(required)* → type *list of type identifier*

17. [**Threat Actor**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_k017w16zutw)
    - If `first_seen` and `last_seen` are both defined, `last_seen` must be greater than or equal to `first_seen`

18. [**Tool**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_z4voa9ndw8v)
    - Needs property `kill_chain_phases` *(optional)* → type *list of type kill-chain-phase*

19. [**Vulnerability**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_q5ytzmajn6re)
    - This one should be complete.

### STIX Relationship Objects (SROs)

There are 2 SROs, namely `relationship` and `sighting`, and are set up via the TypeScript in app.component.ts

The list of what can be the source and target in a `relationship` between SDOs, as well as what type of relationship it is, are in relationship.service.ts

The SROs are not currently set up to allow for the additional properties as denoted in [Section 5 in the STIX 2.1 documentation](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_cqhkqvhnlgfh). Currently, they only send the `relationship_type`, the `source_ref`, and the `target_ref` (if a *relationship*).

### STIX Cyber-observable Objects (SCOs)

There is currently nothing set up for SCOs. For information on SCOs, please visit [Section 6 in the STIX 2.1 documentation](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_mlbmudhl16lr).