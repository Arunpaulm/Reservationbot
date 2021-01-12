# Reservationbot

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A python project to manage and validate the data provided by the Natural language processing (NLP). Reservationbot provides multiple API endpoints with a parser based on use cases.

**Requirements:**

- [x] Python v3.9.1

- [x] Django v3.1.5

- [x] Djangorestframework v3.12.2

- [x] Docker v20.10.2

- [x] Docker compose v1.27.4

**Dev Requirements:**

- [x] autopep8

- [x] Prettier

## Development Environment setup

Follow the instructions as mentioned below:

- Install and Setup [Docker](https://docs.docker.com/engine/install/)

- Download the project to local

```cmd
$ git clone https://github.com/Arunpaulm/Reservationbot.git
```

- Initiate the docker container

```cmd
sudo docker-compose up
```

note: using --detach runs the container in background. to attach use `docker attach reservationbot_reservationbot_1`

- Build the project within docker container

```cmd
sudo docker-compose build
```

- List the project in docker container

```cmd
sudo docker-compose images
```

Use the http://localhost:8080/ to check django up status

- Run Unit testing in Terminal using

```cmd
python manage.py test
```

## Api Endpoints

> **Finite values entity parser**

- [x] `http://localhost:8000/finite_values_entity`

**Example:**

> Request:

| Request type | POST                                                                                                                                                                                                                                                                                                                                                                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| url          | http://localhost:8000/finite_values_entity                                                                                                                                                                                                                                                                                                                                    |
| payload      | {"invalid_trigger":"invalid_ids_stated","key":"ids_stated","name":"govt_id","reuse":true,"support_multiple":false,"pick_first":true,"supported_values":["pan","aadhaar","college","corporate","dl","voter","passport","local"],"type":["id"],"validation_parser":"finite_values_entity","values":[{"entity_type":"id","value":"local"},{"entity_type":"id","value":"other"}]} |
| headers      | 'Content-Type': 'application/json'                                                                                                                                                                                                                                                                                                                                            |

&nbsp;

> Response:

```response
{
	"filled": true,
	"partially_filled": false,
	"trigger": "",
	"parameters": {
		"age_stated": "21"
	}
}
```

&nbsp;

> **Numeric values entity parser**

- [x] localhost:8000/numeric_values_entity

**Example:**

> Request:

| Request type | POST                                                                                                                                                                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| url          | http://localhost:8000/numeric_values_entity                                                                                                                                                                                                                                                                              |
| payload      | {"invalid_trigger":"invalid_age","key":"age_stated","name":"age","reuse":true,"pick_first":true,"support_multiple":false,"type":["number"],"validation_parser":"numeric_values_entity","constraint":"x>=18 and x<=30","var_name":"x","values":[{"entity_type":"number","value":21},{"entity_type":"number","value":21}]} |
| headers      | 'Content-Type': 'application/json'                                                                                                                                                                                                                                                                                       |

&nbsp;

> Response:

```response
{
	"filled": true,
	"partially_filled": false,
	"trigger": "",
	"parameters": {
		"age_stated": "21"
	}
}
```

&nbsp;
**Docker:**

```
 Docker Repository: arunpaulm/reservationbot
 Tag: latest
 Docker image size: 930.53 MB
 Docker image compressed size: 342.28 MB
 Linked with : Github
 Autobuild trigger enabled with master branch
```
