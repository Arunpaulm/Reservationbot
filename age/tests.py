# from django.test import Client, TestCase
from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APITestCase


class TestCasesAge(APITestCase):
    """ Test module for age finite values entity parser """

    def setUp(self):
        self.const_payload = {
            "invalid_trigger": "invalid_age",
            "key": "age_stated",
            "name": "age",
            "reuse": True,
            "pick_first": True,
            "support_multiple": False,
            "type": [
                "number"
            ],
            "validation_parser": "numeric_values_entity",
            "constraint": "x>=18 and x<=30",
            "var_name": "x",
            "values": []
        }

        self.payload_case_1 = {
            "values": [
                {
                    "entity_type": "number",
                    "value": 21
                }
            ]
        }

        self.expected_result_1 = {
            "filled": True,
            "partially_filled": False,
            "trigger": "",
            "parameters": {'age_stated':21}
        }

        self.payload_case_2 = {
            "values": [
                {
                    "entity_type": "number",
                    "value": -1
                }
            ]
        }

        self.expected_result_2 = {
            "filled": False,
            "partially_filled": True,
            "trigger": "invalid_age",
            "parameters": {}
        }

        self.payload_case_3 = {
            "values": []
        }

        self.expected_result_3 = {
            "filled": False,
            "partially_filled": False,
            "trigger": "invalid_age",
            "parameters": {}
        }

        self.payload_case_4 = {
            "values": [
                {
                    "entity_type": "number",
                    "value": 22
                },
                {
                    "entity_type": "number",
                    "value": 10
                }
            ]
        }

        self.expected_result_4 = {
            "filled": False,
            "partially_filled": True,
            "trigger": "invalid_age",
            "parameters": { 'age_stated': 22 }
        }

        self.payload_case_5 = {
            "values": [
                {
                    "entity_type": "number",
                    "value": 24
                },
                {
                    "entity_type": "number",
                    "value": 22
                }
            ]
        }

        self.expected_result_5 = {
            "filled": True,
            "partially_filled": False,
            "trigger": "",
            "parameters": {'age_stated': 24} 
        }

        self.payload_fail_case = {
            "values": [ "number", 24 ]
        }


    def test_age_api_test_case_1(self):
        print('Test case 1 => Age ')
        self.const_payload['values'] = self.payload_case_1['values']
        response = self.client.post(
            reverse('age'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_1)

    def test_age_api_test_case_2(self):
        print('Test case 2 => Age ')
        self.const_payload['values'] = self.payload_case_2['values']
        response = self.client.post(
            reverse('age'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_2)

    def test_age_api_test_case_3(self):
        print('Test case 3 => Age ')
        self.const_payload['values'] = self.payload_case_3['values']
        response = self.client.post(
            reverse('age'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_3)

    def test_age_api_test_case_4(self):
        print('Test case 4 => Age ')
        self.const_payload['values'] = self.payload_case_4['values']
        response = self.client.post(
            reverse('age'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_4)

    def test_age_api_test_case_5(self):
        print('Test case 5 => Age ')
        self.const_payload['values'] = self.payload_case_5['values']
        response = self.client.post(
            reverse('age'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.expected_result_5)

    def test_age_api_fail_test_6(self):
        print('Test case 6 => Age ')
        self.const_payload['values'] = self.payload_fail_case['values']
        response = self.client.post(
            reverse('age'),
            data=json.dumps(self.const_payload),
            content_type='application/json'
        )
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
