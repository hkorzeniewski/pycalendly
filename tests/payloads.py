get_user_paylod = {
    "resource": {
        "uri": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
        "name": "John Doe",
        "slug": "acmesales",
        "email": "test@example.com",
        "scheduling_url": "https://calendly.com/acmesales",
        "timezone": "America/New York",
        "avatar_url": "https://01234567890.cloudfront.net/uploads/user/avatar/0123456/a1b2c3d4.png",
        "created_at": "2019-01-02T03:04:05.678123Z",
        "updated_at": "2019-08-07T06:05:04.321123Z",
        "current_organization": "https://api.calendly.com/organizations/AAAAAAAAAAAAAAAA",
        "resource_type": "User",
    }
}

get_event_types_payload = {
    "collection": [
        {
            "uri": "https://api.calendly.com/event_types/AAAAAAAAAAAAAAAA",
            "name": "15 Minute Meeting",
            "active": True,
            "booking_method": "instant",
            "slug": "acmesales",
            "scheduling_url": "https://calendly.com/acmesales",
            "duration": 30,
            "kind": "solo",
            "pooling_type": "round_robin",
            "type": "StandardEventType",
            "color": "#fff200",
            "created_at": "2019-01-02T03:04:05.678123Z",
            "updated_at": "2019-08-07T06:05:04.321123Z",
            "internal_note": "Internal note",
            "description_plain": "15 Minute Meeting",
            "description_html": "<p>15 Minute Meeting</p>",
            "profile": {
                "type": "User",
                "name": "Tamara Jones",
                "owner": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
            },
            "secret": True,
            "deleted_at": None,
            "admin_managed": False,
            "custom_questions": [
                {
                    "name": "Company Name",
                    "type": "string",
                    "position": 0,
                    "enabled": True,
                    "required": True,
                    "answer_choices": [],
                    "include_other": False,
                },
            ],
        }
    ],
    "pagination": {
        "count": 20,
        "next_page": "https://api.calendly.com/event_types?count=1&page_token=sNjq4TvMDfUHEl7zHRR0k0E1PCEJWvdi",
        "previous_page": "https://api.calendly.com/event_types?count=1&page_token=VJs2rfDYeY8ahZpq0QI1O114LJkNjd7H",
        "next_page_token": "sNjq4TvMDfUHEl7zHRR0k0E1PCEJWvdi",
        "previous_page_token": "VJs2rfDYeY8ahZpq0QI1O114LJkNjd7H",
    },
}


create_single_use_link_payload = {
    "resource": {
        "booking_url": "https://calendly.com/d/48k-rx3-pm5/konsultacja-90-min",
        "owner": "https://api.calendly.com/event_types/5f599ff5-9e71-454c-9f4f-59d761109a1c",
        "owner_type": "EventType",
    }
}

list_all_webhooks_payload = {
    "collection": [
        {
            "uri": "https://api.calendly.com/webhook_subscriptions/AAAAAAAAAAAAAAAA",
            "callback_url": "https://blah.foo/bar",
            "created_at": "2019-08-24T14:15:22.123456Z",
            "updated_at": "2019-08-24T14:15:22.123456Z",
            "retry_started_at": "2019-08-24T14:15:22.123456Z",
            "state": "active",
            "events": ["invitee.created"],
            "scope": "user",
            "organization": "https://api.calendly.com/organizations/AAAAAAAAAAAAAAAA",
            "user": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
            "creator": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
        }
    ],
    "pagination": {
        "count": 20,
        "next_page": "https://api.calendly.com/webhook_subscriptions?count=1&page_token=sNjq4TvMDfUHEl7zHRR0k0E1PCEJWvdi",
        "previous_page": "https://api.calendly.com/webhook_subscriptions?count=1&page_token=VJs2rfDYeY8ahZpq0QI1O114LJkNjd7H",
        "next_page_token": "sNjq4TvMDfUHEl7zHRR0k0E1PCEJWvdi",
        "previous_page_token": "VJs2rfDYeY8ahZpq0QI1O114LJkNjd7H",
    },
}

get_webhook_subscription_payload = {
    "resource": {
        "uri": "https://api.calendly.com/webhook_subscriptions/AAAAAAAAAAAAAAAA",
        "callback_url": "https://blah.foo/bar",
        "created_at": "2019-08-24T14:15:22.123456Z",
        "updated_at": "2019-08-24T14:15:22.123456Z",
        "retry_started_at": "2019-08-24T14:15:22.123456Z",
        "state": "active",
        "events": ["invitee.created"],
        "scope": "user",
        "organization": "https://api.calendly.com/organizations/AAAAAAAAAAAAAAAA",
        "user": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
        "creator": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
    }
}

create_webhook_subscription_payload = {
    "resource": {
        "uri": "https://api.calendly.com/webhook_subscriptions/AAAAAAAAAAAAAAAA",
        "callback_url": "https://blah.foo/bar",
        "created_at": "2019-08-24T14:15:22.123456Z",
        "updated_at": "2019-08-24T14:15:22.123456Z",
        "retry_started_at": "2019-08-24T14:15:22.123456Z",
        "state": "active",
        "events": ["invitee.created"],
        "scope": "user",
        "organization": "https://api.calendly.com/organizations/AAAAAAAAAAAAAAAA",
        "user": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
        "creator": "https://api.calendly.com/users/AAAAAAAAAAAAAAAA",
    }
}
