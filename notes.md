sudo docker-compose run reservationbot django-admin startproject roomReservationBot .



> sudo docker-compose run reservationbot django-admin startproject roomReservationBot .

WARNING: Found orphan containers (minibot_web_1) for this project. If you removed or renamed this service in your compose file, you can run this command with the --remove-orphans flag to clean it up.
Building reservationbot
Step 1/7 : FROM python:3.9.1
 ---> d1eef6fb8dbe
Step 2/7 : ENV PYTHONUNBUFFERED 1
 ---> Running in 29c255b83b6e
Removing intermediate container 29c255b83b6e
 ---> de0800413592
Step 3/7 : RUN mkdir /roomReservationBot
 ---> Running in 87d7f84436cf
Removing intermediate container 87d7f84436cf
 ---> 77abe86a2b02
Step 4/7 : WORKDIR /roomReservationBot
 ---> Running in ee82d2e8076d
Removing intermediate container ee82d2e8076d
 ---> 4737deafbe59
Step 5/7 : COPY requirements.txt /roomReservationBot/
 ---> e4c201371c35
Step 6/7 : RUN pip install -r requirements.txt
 ---> Running in e98515f8148b
Collecting django==3.1.5
  Downloading Django-3.1.5-py3-none-any.whl (7.8 MB)
Collecting djangorestframework==3.12.2
  Downloading djangorestframework-3.12.2-py3-none-any.whl (957 kB)
Collecting asgiref<4,>=3.2.10
  Downloading asgiref-3.3.1-py3-none-any.whl (19 kB)
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.1-py3-none-any.whl (42 kB)
Collecting pytz
  Downloading pytz-2020.5-py2.py3-none-any.whl (510 kB)
Installing collected packages: sqlparse, pytz, asgiref, django, djangorestframework
Successfully installed asgiref-3.3.1 django-3.1.5 djangorestframework-3.12.2 pytz-2020.5 sqlparse-0.4.1
Removing intermediate container e98515f8148b
 ---> 06295e3ef9a4
Step 7/7 : COPY . /roomReservationBot/
 ---> 224c11b87789

Successfully built 224c11b87789
Successfully tagged minibot_reservationbot:latest
WARNING: Image for service reservationbot was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Creating minibot_reservationbot_run ... done


python manage.py migrate
python manage.py createsuperuser


python manage.py startapp documents
python manage.py startapp age

docker-compose up


python3 manage.py makemigrations
python manage.py migrate


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



{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "ids_stated": ["COLLEGE"]
    }
}




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


{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "age_stated": 23
    }
}

'documents',
    'age'

    from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents', include('documents.urls')),
    path('age', include('age.urls'))
]