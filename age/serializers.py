from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
from .models import Age

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
    value = serializers.IntegerField(default=0)


'''
creating serializers for managing and validating the json data
serializer create for Payload model
{
  "invalid_trigger": "invalid_age",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "support_multiple": false,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 21
    },
     {
      "entity_type": "number",
      "value": 21
    }
  ]
}
'''


class AgeSerializer(serializers.HyperlinkedModelSerializer):
    type = serializers.ListField(child=serializers.CharField(max_length=10))
    values = serializers.ListField(child=ValuesArray())

    class Meta:
        model = Age
        fields = ('invalid_trigger', 'key', 'name', 'reuse', 'support_multiple',
                  'pick_first', 'type', 'validation_parser', 'constraint', 'var_name', 'values')
