from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from builders.stix_builder_factory import StixBuilderFactory
from builders.relationship_builder import RelationshipBuilder
from stix2 import Bundle

# Create your views here.
@csrf_exempt
def add_stix_data(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        
        # Do something with the data
        # For now, we'll just print it
        stix_dict = {index: [] for index in range(len(data['objects']))}
        for _ in range(data['dataset']):
            for index, object in enumerate(data['objects']):
                stix_dict[index].append(StixBuilderFactory.create(object['type'],object['name']))

        relationship_list = []
        for relationship in (data['relationships']):
            for index in range(len(stix_dict[relationship['source']])):
                source = stix_dict[relationship['source']][index]
                target = stix_dict[relationship['target']][index]
                relationship_list.append(RelationshipBuilder(source, target, relationship['relationship']).create())

        stix_list = []
        for sublist in stix_dict.values():
            stix_list.extend(item for item in sublist if item is not None)

        bundle = Bundle(stix_list, relationship_list)
        print(bundle.serialize(pretty=True))

        return JsonResponse({"message": "Data received."})
    else:
        return JsonResponse({"message": "Only POST requests are allowed."}, status=400)