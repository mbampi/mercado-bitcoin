
import datetime as dt


class Response:

    def __init__(self, json):
        server_unix_timestamp = json['server_unix_timestamp']
        self.date_time = dt.datetime.utcfromtimestamp(server_unix_timestamp)
        self.status_code = json['status_code']

        if self.status_code != '100':  # Success
            self.error_message = json['error_message']
        else:
            self.error_message = None

        self.response_data = json['response_data']
