from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import serializers

from .models import Document
from .serializers import DocumentSerializer

from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]


def validate_finite_values_entity(values: List[Dict], supported_values: List[str] = None,
                                  invalid_trigger: str = None, key: str = None,
                                  support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
    # created flag for fill status
    filled = False
    partially_filled = False
    # invalid_ids_stated will hold the valid document type
    invalid_ids_stated = list()
    params = dict()

    '''
    The for loop iterates the values from request and
    checks document type is supported
    in positive scenario - values are appended to invalid_ids_stated variable
    '''
    for value in values:
        if value['entity_type'] == 'id':
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
    validationCondition = not len(values) == 0 and ( pick_first and len(invalid_ids_stated) > 0 or len(values) == len(invalid_ids_stated))
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
def getDocumentsDetails(request, pk=None, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        # serializer_context = {
        #     'request': request,
        # }
        # doc = Document.objects.all()
        print(request.data)
        filled, partially_filled, trigger, parameters = validate_finite_values_entity(
            request.data['values'], request.data['supported_values'], request.data['invalid_trigger'], request.data['key'], request.data['support_multiple'], request.data['pick_first'])

        return Response({'filled': filled, 'partially_filled': partially_filled, 'trigger': trigger, 'parameters': parameters}, status=status.HTTP_200_OK)
    #     serializer = DocumentSerializer(data=request.data) #, context=serializer_context) # data=request.data
    #     # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    #     if serializer.is_valid():
    #         print('valid')
    #         # serializer.save()
    #         # validate_finite_values_entity(serializer.data['values'],serializer.data['values'],serializer.data['values'],serializer.data['values'],serializer.data['values'],serializer.data['values'],)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else :
    #         print(serializer.validated_data)
    #         return Response({ "error": serializer.data['invalid_trigger'] })
    # return Response({ "internal error" })
