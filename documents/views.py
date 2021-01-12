from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
# from rest_framework.request import Request
from rest_framework.decorators import api_view
# from rest_framework import serializers

# from .models import Document
from .serializers import DocumentSerializer

from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]

'''
validate_finite_values_entity function performs the processing data provided in the request
returns (filled, partially_filled, trigger, params) => (bool, bool, str, Dict)
'''


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None,
                                  support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
    # created flag for fill status
    filled = False
    partially_filled = False
    # invalid_ids_stated will hold the valid document type
    invalid_ids_stated = list()
    params = dict()
    kwargs_items = {}
    # unwraping kwargs to kwargs_items dict
    for ikey, ivalue in kwargs.items():
        kwargs_items[ikey] = ivalue

    '''
    The for loop iterates the values from request and
    checks document type is supported
    in positive scenario - values are appended to invalid_ids_stated variable
    '''
    for value in values:
        if value['entity_type'] in kwargs_items['type']:
            partially_filled = True
            document_name = value['value']
            if value['value'] == document_name in supported_values:
                invalid_ids_stated.append(document_name.upper())
        if pick_first:
            break

    '''
    Checking the values based on valid data 
    filled and partially_filled flags will be set with boolean data
    '''
    validationCondition = not len(values) == 0 and (pick_first and len(
        invalid_ids_stated) > 0 or len(values) == len(invalid_ids_stated))
    # validationCondition = not len(values) == 0 and len(values) == len(invalid_ids_stated)
    if validationCondition:
        filled = True
        partially_filled = False
        params = {
            key: invalid_ids_stated
        }
        invalid_trigger = ''
    elif len(invalid_ids_stated) > 0:
        params = {
            key: invalid_ids_stated
        }
    # Finalizing the result by checking
    if pick_first == True:
        params[key] = ''.join(map(str, params[key]))

    # removed the key from value it it is empty
    if len(params[key]) == 0:
        del params[key]
    # (filled, partially_filled, trigger, params)
    return (filled, partially_filled, invalid_trigger, params)


'''
Expected Input
URL : localhost:8000/finite_values_entity
Request type: POST

Body:
{
  "invalid_trigger": "invalid_ids_stated",
  "key": "ids_stated",
  "name": "govt_id",
  "reuse": true,
  "support_multiple": true,
  "pick_first": false,
  "supported_values": [
    "pan",
    "aadhaar",
    "college",
    "corporate",
    "dl",
    "voter",
    "passport",
    "local"
  ],
  "type": [
    "id"
  ],
  "validation_parser": "finite_values_entity",
  "values": [                       
  {                     
    "entity_type": "id",
    "value": "local"  
  },
{                     
    "entity_type": "id",
    "value": "local"  
  }                   
]
}
'''


@api_view(['POST'])
def getDocumentsDetails(request):
    """
    Handler for POST request from endpoint - finite_values_entity
    """
    if request.method == 'POST':
        print(request.data)
        # , context=serializer_context) # data=request.data
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            filled, partially_filled, trigger, parameters = validate_finite_values_entity(
                serializer.data['values'], serializer.data['supported_values'], serializer.data['invalid_trigger'], serializer.data['key'], serializer.data['support_multiple'], serializer.data['pick_first'], type=serializer.data['type'])

            return Response({'filled': filled, 'partially_filled': partially_filled, 'trigger': trigger, 'parameters': parameters}, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
