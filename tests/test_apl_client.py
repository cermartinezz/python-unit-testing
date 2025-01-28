import unittest
from unittest import TestCase
from unittest.mock import patch

import requests.exceptions

from src.api_client import get_location


class ApiClientTest(TestCase):

    @patch("src.api_client.requests.get")
    def test_get_location_returns_expected_result(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "cityName": "Florida",
            "regionName": "Miami",
        }
        data = get_location("8.8.8.8")
        self.assertEqual(data.get("country"), "USA")
        self.assertEqual(data.get("city"), "Florida")
        self.assertEqual(data.get("region"), "Miami")

        mock_get.assert_called_once_with("http://freeipapi.com/api/json/8.8.8.8")

    @patch("src.api_client.requests.get")
    def test_get_location_returns_side_effect(self, mock_get):
        mock_get.side_effect = [
            requests.exceptions.RequestException("Service Unavailable"),
            unittest.mock.Mock(
                status_code=200,
                json=lambda: {
                    "countryName": "USA",
                    "cityName": "Florida",
                    "regionName": "Miami",
                },
            ),
        ]

        with self.assertRaises(requests.RequestException):
            get_location("8.8.8.8")

        data = get_location("8.8.8.10")
        self.assertEqual(data.get("country"), "USA")
        self.assertEqual(data.get("city"), "Florida")
        self.assertEqual(data.get("region"), "Miami")
