class CalendlyConfig(object):
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": "Bearer " + self.token}
