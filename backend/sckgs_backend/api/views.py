from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from services.stix_builder_factory import StixBuilderFactory
from services.relationship_builder import RelationshipBuilder
from services.stix_proportions import StixProportions
from stix2 import Bundle
from itertools import cycle
import pyperclip

# Create your views here.
@csrf_exempt
def add_stix_data(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        dataset_size = data['dataset']
        stix_objects = data['objects']
        relationships = data['relationships']

        proportions = {}
        for stix in (stix_objects):
            proportion = StixProportions().get_proportions(stix['type'])
            proportions[stix_objects.index(stix)] = proportion

        adjusted_proportions = StixProportions.adjust_proportions(proportions)
        stix_dict = {index: [] for index in range(len(stix_objects))}
        total_created = 0
        stix_totals = {}
        for stix in stix_objects:
            count = int(dataset_size * adjusted_proportions[stix_objects.index(stix)])

            stix_totals[stix['type']] = count
            total_created += count
            if stix['type'] in  stix_totals:
                stix_totals[stix['type']] += count
            else:
                stix_totals[stix['type']] = count

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
        print(stix_totals)
        # total of created stix objects
        print("Total created: "+ str(total_created))
        # completed bundle
        bundle = Bundle(stix_list, relationship_list)
        # copies to clip board for testing
        pyperclip.copy(bundle.serialize(pretty=True))

        return JsonResponse({"message": "Data received.", "stix_totals": stix_totals, "bundle": bundle.serialize(pretty=True)})
    else:
        return JsonResponse({"message": "Only POST requests are allowed."}, status=400)