from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_stix_data(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        
        # Do something with the data
        # For now, we'll just print it
        print(data)
        
        return JsonResponse({"message": "Data received."})
    else:
        return JsonResponse({"message": "Only POST requests are allowed."}, status=400)