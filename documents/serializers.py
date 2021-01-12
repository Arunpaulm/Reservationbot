from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
from .models import Document


'''
 "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
'''
class ValuesArray(serializers.Serializer):
    entity_type = serializers.CharField(max_length=20)
    value = serializers.CharField(max_length=10)


'''
creating serializers for managing and validating the json data
serializer create for Payload model
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
      "value": "college"
    }
  ]
}
'''


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    supported_values = serializers.ListField(child=serializers.CharField(max_length=15))
    type = serializers.ListField(child=serializers.CharField(max_length=5))
    values = serializers.ListField(child=ValuesArray())

    class Meta:
        model = Document
        fields = ('invalid_trigger', 'key', 'name', 'reuse', 'support_multiple',
                  'pick_first', 'supported_values', 'type', 'validation_parser', 'values')
