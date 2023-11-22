import json

import requests

from calendly.constants import API, USERS_ME, SCHEDULING_LINKS, WEBHOOKS
from calendly.config import CalendlyConfig

class Calendly(CalendlyConfig):
    def __init__(self, token: str):
        super().__init__(token)
        self.user = self.get_users_me()
        self.organization = self.user["resource"]["current_organization"]
        self.user_id = self.user["resource"]["uri"]

    def get_users_me(self):
        response = requests.get(USERS_ME, headers=self.headers)
        response = response.json()
        return response

    def get_users(self, uuid: str):
        url = API + f"users/{uuid}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_event_types(self):
        url = (
            API
            + f"event_types?organization={self.organization}&user={self.user_id}"
        )
        data = {
            "organization": self.organization,
            "user": self.user,
        }
        response = requests.get(url, headers=self.headers, data=json.dumps(data))
        return response.json()

    def create_single_use_link(self, event_name: str):
        event_types = self.get_event_types()
        for i, event_type in enumerate(event_types["collection"]):
            if event_type["name"] == event_name:
                owner_url = event_type["uri"]
        data = {"max_event_count": 1, "owner": owner_url, "owner_type": "EventType"}
        response = requests.post(SCHEDULING_LINKS, headers=self.headers, data=data)
        return response.json()

    def list_all_webhooks(self, scope: str = "organization"):
        if scope not in ["organization", "user"]:
            raise ValueError("scope must be 'organization' or 'user'")
        elif scope == "organization":
            url = WEBHOOKS + f"?organization={self.organization}&scope={scope}"
        else:
            url = (
                WEBHOOKS
                + f"?organization={self.organization}&scope={scope}&user={self.user_id}"
            )
        print(self.organization)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_webhook_subscription(self, webhook_uri: str):
        response = requests.get(webhook_uri, headers=self.headers)
        return response.json()

    def create_webhook_subscription(self, url: str, scope: str = "organization"):
        if scope not in ["organization", "user"]:
            raise ValueError("scope must be 'organization' or 'user'")
        data = {
            "url": url,
            "events": ["invitee.created", "invitee.canceled"],
            "organization": self.organization,
            "user": self.user_id,
            "scope": scope,
        }
        try:
            response = requests.post(WEBHOOKS, headers=self.headers, data=data)
            print(response)
            return response.json()
        except Exception as e:
            print("Please upgrade your Calendly account to Standard")
            return e

    def delete_webhook_subscription(self, webhook_uri: str):
        url = webhook_uri
        response = requests.delete(url, headers=self.headers)
        print("Deleted webhook subscription")
        return response
