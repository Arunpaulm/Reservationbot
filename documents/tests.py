from django.test import Client  # , TestCase
from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase


class TestCasesDocuments(APITestCase):
    """ Test module for Documents finite values entity parser """

    def setUp(self):
        self.const_payload = {
            "invalid_trigger": "invalid_ids_stated",
            "key": "ids_stated",
            "name": "govt_id",
            "reuse": True,
            "support_multiple": True,
            "pick_first": False,
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
            "values": []
        }

        self.payload_case_1 = {
            "values": [
                {
                    "entity_type": "id",
                    "value": "college"
                }
            ]
        }

        self.expected_result_1 = {
            "filled": True,
            "partially_filled": False,
            "trigger": "",
            "parameters": {'ids_stated': ['COLLEGE']}
        }

        self.payload_case_2 = {
            "values": [
                {
                    "entity_type": "id",
                    "value": "other"
                }
            ]
        }

        self.expected_result_2 = {
            "filled": False,
            "partially_filled": True,
            "trigger": "invalid_ids_stated",
            "parameters": {}
        }

        self.payload_case_3 = {
            "values": []
        }

        self.expected_result_3 = {
            "filled": False,
            "partially_filled": False,
            "trigger": "invalid_ids_stated",
            "parameters": {}
        }

        self.payload_case_4 = {
            "values": [
                {
                    "entity_type": "id",
                    "value": "college"
                },
                {
                    "entity_type": "id",
                    "value": "other"
                }
            ]
        }

        self.expected_result_4 = {
            "filled": False,
            "partially_filled": True,
            "trigger": "invalid_ids_stated",
            "parameters": {}
        }

        self.payload_case_5 = {
            "values": [
                {
                    "entity_type": "id",
                    "value": "college"
                },
                {
                    "entity_type": "id",
                    "value": "aadhaar"
                }
            ]
        }

        self.expected_result_5 = {
            "filled": True,
            "partially_filled": False,
            "trigger": "",
            "parameters": {'ids_stated': ['COLLEGE', 'AADHAAR']}
        }

        self.payload_fail_case = {
            "values": [ "id", "college" ]
        }

    def test_documents_api_test_case_1(self):
        print('Test case 1 => Documents ')
        self.const_payload['values'] = self.payload_case_1['values']
        response = self.client.post(
            reverse('documents'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_1)

    def test_documents_api_test_case_2(self):
        print('Test case 2 => Documents ')
        self.const_payload['values'] = self.payload_case_2['values']
        response = self.client.post(
            reverse('documents'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_2)

    def test_documents_api_test_case_3(self):
        print('Test case 3 => Documents ')
        self.const_payload['values'] = self.payload_case_3['values']
        response = self.client.post(
            reverse('documents'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_3)

    def test_documents_api_test_case_4(self):
        print('Test case 4 => Documents ')
        self.const_payload['values'] = self.payload_case_4['values']
        response = self.client.post(
            reverse('documents'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_4)

    def test_documents_api_test_case_5(self):
        print('Test case 5 => Documents ')
        self.const_payload['values'] = self.payload_case_5['values']
        response = self.client.post(
            reverse('documents'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_5)

    def test_documents_api_fail_test_6(self):
        print('Test case 6 => Documents ')
        self.const_payload['values'] = self.payload_fail_case['values']
        response = self.client.post(
            reverse('documents'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
