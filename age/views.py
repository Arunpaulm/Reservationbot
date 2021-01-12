from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request
from rest_framework.decorators import api_view

# Create your views here.
from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]

'''
validate_numeric_entity function performs the process of data provided in the request

'''


def validate_numeric_entity(values: List[Dict], invalid_trigger: str = None, key: str = None,
                            support_multiple: bool = True, pick_first: bool = False, constraint=None, var_name=None,
                            **kwargs) -> SlotValidationResult:

    # created flag for fill status
    filled = False
    partially_filled = False
    # age_stated will hold the valid age
    age_stated = list()
    params = {key: []}

    '''
    The for loop iterates the values from request and
    check values satisfies the constraint provided in the request
    in positive scenario - values are appended to age_stated variable
    '''
    for value in values:
        if value['entity_type'] == 'number':
            partially_filled = True
            age = value['value']
            is_valid_age = eval(constraint.replace(var_name, str(age)))
            if is_valid_age or constraint == '':
                age_stated.append(age)
        if pick_first:
            break

    '''
    Checking the values based on valid data 
    filled and partially_filled flags will be set with boolean data
    '''
    validationCondition = not len(values) == 0 and ( pick_first and len(age_stated) > 0 or len(values) == len(age_stated))
    # validationCondition = not len(values) == 0 and  len(values) == len(age_stated)
    if validationCondition:
        filled = True
        partially_filled = False
        params = {
            key: age_stated
        }
        invalid_trigger = ''
    elif len(age_stated) > 0:
        params = {
            key: age_stated
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
URL : localhost:8000/numeric_values_entity
Request type: POST

Body:
{
  "invalid_trigger": "invalid_age",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
}
'''


@api_view(['POST'])
def getAgeDetails(request, pk=None, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        # serializer_context = {
        #     'request': request,
        # }
        # doc = Document.objects.all()
        print(request.data)
        filled, partially_filled, trigger, parameters = validate_numeric_entity(
            request.data['values'], request.data['invalid_trigger'], request.data['key'], request.data['support_multiple'], request.data['pick_first'], request.data['constraint'], request.data['var_name'])

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
