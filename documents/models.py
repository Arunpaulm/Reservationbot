from django.db import models

TYPE = (
    ( "id", "id" ),
)

class SupportedValuesArray(models.Model):
    name = models.CharField(max_length=10)

    def natural_key(self):
        return (self.name)


# class TypeArray(models.Model):
#     name = models.CharField(max_length=2, choices=TYPE)

#     def natural_key(self):
#         return (self.name)


class ValuesArray(models.Model):
    entity_type = models.CharField(max_length=2)
    value = models.CharField(max_length=10)

    def __str__(self):
        return self.entity_type, self.value

# SupportedValuesArray = (
#   ("pan", "pan"),
#     ("aadhaar", "aadhaar"),
#     ("college", "college"),
#     ("corporate", "corporate"),
#     ("dl", "dl"),
#     ("voter", "voter"),
#     ("passport", "passport"),
#     ("local", "local")
# )


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

class TypeArray(models.TextChoices):
        id = 'id'


class Document(models.Model):
    invalid_trigger = models.CharField(max_length=20)
    key = models.CharField(max_length=11)
    name = models.CharField(max_length=10)
    reuse = models.BooleanField(default=False)
    support_multiple = models.BooleanField(default=False)
    pick_first = models.BooleanField(default=False)
    # supported_values = models.ManyToManyField(SupportedValuesArray)
    # supported_values = models.CharField(max_length=10, choices=SupportedValuesArray)
    # type = models.ManyToManyField(TypeArray)
    # type = models.ChoiceField(max_length=3, choices=TypeArray.choices)
    validation_parser = models.CharField(max_length=20)
    # values = models.ManyToManyField(ValuesArray)
