import unittest
from unittest.mock import patch
from calendly.calendly import Calendly
from tests.payloads import (
    get_user_paylod,
    get_event_types_payload,
    list_all_webhooks_payload,
    get_webhook_subscription_payload,
    create_webhook_subscription_payload,
)


class TestCalendly(unittest.TestCase):
    def setUp(self) -> None:
        self.organization = "https://api.calendly.com/organizations/AAAAAAAAAAAAAAAA"

    @patch("calendly.calendly.requests.get")
    def test_get_users_me(self, mock_get):
        mock_get.return_value.json.return_value = get_user_paylod
        cal = Calendly("token")
        result = cal.get_users_me()
        self.assertEqual(result, get_user_paylod)

    @patch("calendly.calendly.requests.get")
    def test_get_users(self, mock_get):
        mock_get.return_value.json.return_value = get_user_paylod
        cal = Calendly("token")
        result = cal.get_users("AAAAAAAAAAAAAAAA")
        self.assertEqual(
            result["resource"]["uri"], "https://api.calendly.com/users/AAAAAAAAAAAAAAAA"
        )

    @patch("calendly.calendly.requests.get")
    def test_get_event_types(self, mock_get):
        mock_get.return_value.json.return_value = get_user_paylod
        cal = Calendly("token")
        mock_get.return_value.json.return_value = get_event_types_payload
        result = cal.get_event_types()
        self.assertEqual(result, get_event_types_payload)

    @patch("calendly.calendly.requests.post")
    @patch("calendly.calendly.requests.get")
    def test_create_single_use_link(self, mock_get, mock_post):
        mock_get.return_value.json.return_value = get_user_paylod
        cal = Calendly("token")
        mock_get.return_value.json.return_value = {
            "collection": [{"name": "event_type", "uri": "event_uri"}]
        }
        mock_post.return_value.json.return_value = {"link_data": "data"}
        result = cal.create_single_use_link("event_type")
        self.assertEqual(result, {"link_data": "data"})

    @patch("calendly.calendly.requests.get")
    def test_list_all_webhooks(self, mock_get):
        mock_get.return_value.json.return_value = get_user_paylod
        cal = Calendly("token")
        mock_get.return_value.json.return_value = list_all_webhooks_payload
        result = cal.list_all_webhooks()
        self.assertEqual(result, list_all_webhooks_payload)

    @patch("calendly.calendly.requests.get")
    def test_get_webhook_subscription(self, mock_get):
        mock_get.return_value.json.return_value = get_user_paylod
        cal = Calendly("token")
        mock_get.return_value.json.return_value = get_webhook_subscription_payload
        result = cal.get_webhook_subscription(
            "https://api.calendly.com/webhook_subscriptions/AAAAAAAAAAAAAAAA"
        )
        self.assertEqual(result, get_webhook_subscription_payload)

    @patch("calendly.calendly.requests.post")
    @patch("calendly.calendly.requests.get")
    def test_create_webhook_subscription(self, mock_get, mock_post):
        mock_post.return_value.json.return_value = get_user_paylod
        mock_post.return_value.json.return_value = create_webhook_subscription_payload
        cal = Calendly("token")
        result = cal.create_webhook_subscription(
            "https://api.calendly.com/webhook_subscriptions/AAAAAAAAAAAAAAAA",
            "organization",
        )
        self.assertEqual(result, create_webhook_subscription_payload)
