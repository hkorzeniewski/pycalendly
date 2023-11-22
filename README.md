# Pycalendly

The `Pycalendly` is designed to interact with the Calendly API and provide convenient methods for common operations. 

#### Parameters
- `token` (str): The Calendly API token used for authentication.

#### Example
```python
calendly_instance = Calendly("your_api_token")
```

## Methods

### `get_users_me(self) -> dict`

Retrieve information about the authenticated user.

#### Returns
- `dict`: A dictionary containing user information.

#### Example
```python
user_info = calendly_instance.get_users_me()
```

### `get_users(self, uuid: str) -> dict`

Get information about a specific user based on their UUID.

#### Parameters
- `uuid` (str): The UUID of the user.

#### Returns
- `dict`: A dictionary containing user information.

#### Example
```python
user_info = calendly_instance.get_users("user_uuid")
```

### `get_event_types(self) -> dict`

Retrieve a list of event types associated with the user.

#### Returns
- `dict`: A dictionary containing event type information.

#### Example
```python
event_types_info = calendly_instance.get_event_types()
```

### `create_single_use_link(self, event_name: str) -> dict`

Create a single-use scheduling link for a specific event type.

#### Parameters
- `event_name` (str): The name of the event type for which to create the link.

#### Returns
- `dict`: A dictionary containing information about the created scheduling link.

#### Example
```python
link_info = calendly_instance.create_single_use_link("meeting_event")
```

### `list_all_webhooks(self, scope: str = "organization") -> dict`

List all webhooks associated with the user or organization.

#### Parameters
- `scope` (str, optional): The scope of webhooks to retrieve. Default is "organization".

#### Returns
- `dict`: A dictionary containing information about the retrieved webhooks.

#### Example
```python
webhooks_info = calendly_instance.list_all_webhooks()
```

### `get_webhook_subscription(self, webhook_uri: str) -> dict`

Retrieve information about a specific webhook subscription.

#### Parameters
- `webhook_uri` (str): The URI of the webhook subscription.

#### Returns
- `dict`: A dictionary containing information about the webhook subscription.

#### Example
```python
subscription_info = calendly_instance.get_webhook_subscription("webhook_uri")
```

### `create_webhook_subscription(self, url: str, scope: str = "organization") -> dict`

Create a new webhook subscription.

#### Parameters
- `url` (str): The URL where webhook events will be sent.
- `scope` (str, optional): The scope of the webhook subscription. Default is "organization".

#### Returns
- `dict`: A dictionary containing information about the created webhook subscription.

#### Example
```python
subscription_info = calendly_instance.create_webhook_subscription("https://your-webhook-url", "user")
```

### `delete_webhook_subscription(self, webhook_uri: str) -> dict`

Delete a webhook subscription.

#### Parameters
- `webhook_uri` (str): The URI of the webhook subscription to be deleted.

#### Returns
- `dict`: A dictionary containing information about the deleted webhook subscription.

#### Example
```python
deleted_info = calendly_instance.delete_webhook_subscription("webhook_uri")
```