from calendly.calendly import Calendly


class CalendlyService:
    def __init__(self):
        self.calendly = Calendly()
        self.calendly.get_users()

    def single_use_link(self, event_type):
        events = self.calendly.get_event_types()
        event_url = events["collection"][event_type]["uri"]
        single_use_link = self.calendly.create_single_use_link(owner_url=event_url)
        return single_use_link["resource"]["booking_url"]
