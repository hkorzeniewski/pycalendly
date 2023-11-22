from calendly.calendly import Calendly

# calendly = Calendly(
#     "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNjk2OTIwMzMxLCJqdGkiOiJkNjE3NjJlNy01YTg2LTRjMzgtYTRhMi1hYzg1ZDdmNGY0ODAiLCJ1c2VyX3V1aWQiOiIwNGYwN2I3NS05YmVhLTQzMzgtYmYyNC1mNWRmY2EyZDlkM2EifQ.iF1sJHxgpb2qXwvoSMHWdI9DSMi33zHgaLwF4eW5Dfq3KZ2r1bYsh4-eB7uPtBv-I7HImOAHBhmx2sdA2cQJYw" )

calendly = Calendly(
    "eyJraWQiOiIxY2UxZTEzNjE3ZGNmNzY2YjNjZWJjY2Y4ZGM1YmFmYThhNjVlNjg0MDIzZjdjMzJiZTgzNDliMjM4MDEzNWI0IiwidHlwIjoiUEFUIiwiYWxnIjoiRVMyNTYifQ.eyJpc3MiOiJodHRwczovL2F1dGguY2FsZW5kbHkuY29tIiwiaWF0IjoxNzAwNTg1OTU2LCJqdGkiOiI1ZGVhZjdkMS0wNTEzLTQxOGEtOTEwNi1mYmI5MGViN2I5NzYiLCJ1c2VyX3V1aWQiOiJjOWM2MjgzNy0yYjZjLTQyMzMtYjgwOS02MTU5MjRmZTgyMzAifQ.dvaH74WBqw43WuTnCysKcJ1ES__dE-p7AFrcst7uYRBYOzq09X937R5sQ7-ufKUTPX407kTwbpCrgtcjc29wwQ"
)


# print(calendly.get_users_me())
# print(calendly.get_users("c9c62837-2b6c-4233-b809-615924fe8230"))
# print(calendly.get_event_types())
# calendly.get_event_types()
# print(calendly.create_single_use_link("Konsultacja 90-min"))

# print(calendly.list_all_webhooks(scope="user"))

webhooks = calendly.list_all_webhooks(scope="organization")

# print(webhooks)

print(calendly.get_webhook_subscription(webhook_uri=webhooks["collection"][0]["uri"]))
# print(
#     calendly.create_webhook_subscription(
#         url="https://blah.foo/bar", scope="organization"
#     )
# )

# print(calendly.list_all_webhooks(scope="organization"))

# print(
#     calendly.delete_webhook_subscription(
#         webhook_uri="https://api.calendly.com/webhook_subscriptions/0d5e01ca-5642-4bb6-9dd8-a70bcd733771"
#     )
# )
