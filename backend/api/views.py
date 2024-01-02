from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from services.stix_builder_factory import StixBuilderFactory
from services.relationship_builder import RelationshipBuilder
from services.stix_weights import StixWeights
from stix2 import Bundle
from itertools import cycle
import pyperclip

# Create your views here.
@csrf_exempt
def add_stix_data(request):
    if request.method == 'POST':
        # Parse the incoming JSON data.
        data = json.loads(request.body)
        dataset_size = data['dataset']
        stix_objects = data['objects']
        relationships = data['relationships']
        
        # Get the SDOs weights.
        weights = StixWeights.get_weights(stix_objects)
        # Adjust the SDOs weights
        adjusted_weights = StixWeights.adjust_weights(weights)

        # Dictionary to store created SDOs.
        # SDOs are stored in the stix_dict based on their index in the stix_objects array.
        stix_dict = {index: [] for index in range(len(stix_objects))}
        # The total number of created SDOs.
        total_created = 0
        # Dictionary of SDO type totals.
        type_totals = {}
        # create SDOs.
        for stix in stix_objects:
            # Determine how many SDOs to create base on its type.
            count = int(dataset_size * adjusted_weights[stix_objects.index(stix)])
            # Add count to total_created.
            total_created += count
            # Store count in type_totals dictionary.
            if stix['type'] in  type_totals:
                type_totals[stix['type']] += count
            else:
                type_totals[stix['type']] = count

            for _ in range(count):
                stix_dict[stix_objects.index(stix)].append(StixBuilderFactory.create(stix))

        relationship_list = []
        for relationship in (relationships):
            source_list = stix_dict[relationship['source']]
            target_list = stix_dict[relationship['target']]
            cycle_source = cycle(source_list)
            cycle_target = cycle(target_list)

            for _ in range(max(len(source_list), len(target_list))):
                relationship_list.append(RelationshipBuilder(next(cycle_source), next(cycle_target), relationship['relationship']).create())

        stix_list = []
        for sublist in stix_dict.values():
            stix_list.extend(item for item in sublist if item is not None)

        # dictionary of stix totals
        print(type_totals)
        # total of created stix objects
        print("Total created: "+ str(total_created))
        # completed bundle
        bundle = Bundle(stix_list, relationship_list)
        # copies to clip board for testing
        pyperclip.copy(bundle.serialize(pretty=True))

        return JsonResponse({"message": "Data received.", "stix_totals": type_totals, "bundle": bundle.serialize(pretty=True)})
    else:
        return JsonResponse({"message": "Only POST requests are allowed."}, status=400)