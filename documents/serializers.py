from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Document


'''
Created a model for the json input
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


class ValuesArray(serializers.Serializer):
    entity_type = serializers.CharField(max_length=2)
    value = serializers.CharField(max_length=10)


class DocumentModel(serializers.Serializer):
    # type = serializers.ListField(
    #     child=serializers.IntegerField(min_value=0, max_value=1)
    # )
    values = ValuesArray(many=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Document.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        # instance.type = validated_data.get('type', instance.type)
        instance.values = validated_data.get('values', instance.values)
        instance.save()
        return instance
    # class Meta:
    #     model = Document
    #     fields = '__all__'


'''
creating serializers for managing and validating the json data
serializer create for Payload model
'''


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        # fields = '__all__'
        fields = ('invalid_trigger', 'key', 'name', 'reuse',
                  'support_multiple', 'pick_first', 'type', 'validation_parser')
        # 'invalid_trigger', 'key', 'name', 'reuse', 'support_multiple', 'pick_first', 'supported_values', 'type', 'validation_parser', 'values'
