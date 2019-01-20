import bs4
import requests

from datetime import datetime


class PyDSB:
    BASE_URL = "https://iphone.dsbcontrol.de/iPhoneService.svc/DSB"
    ZERO_VALUE = "00000000-0000-0000-0000-000000000000"

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
        self.token = None

    def login(self):
        r = requests.get(f"{self.BASE_URL}/authid/{self.username}/{self.password}")
        token = r.text.strip("\"")

        if token == self.ZERO_VALUE:
            raise LoginError("Username or password is wrong")

        self.token = token

    def get_timetables(self):
        r = requests.get(f"{self.BASE_URL}/timetables/{self.token}")
        data = r.json()

        return [
            {
                "is_html": timetable["ishtml"],
                "date": self._get_as_datetime(timetable["timetabledate"]),
                "group": timetable["timetablegroupname"],
                "title": timetable["timetabletitle"],
                "url": timetable["timetableurl"]
            }
            for timetable in data
        ]

    def get_news(self):
        r = requests.get(f"{self.BASE_URL}/news/{self.token}")
        data = r.json()

        return [
            {
                "headline": news["headline"],
                "date": self._get_as_datetime(news["newsdate"], with_second=True),
                "id": news["newsid"],
                "image_url": news["newsimageurl"],
                "short_message": news["shortmessage"],
                "wholemessage": news["wholemessage"]
            }
            for news in data
            if news["newsid"] != self.ZERO_VALUE
        ]

    def _get_as_datetime(self, date_string, with_second=False):
        date_format = "%d.%m.%Y %H:%M"
        if with_second:
            date_format += ":%S"

        return datetime.strptime(date_string, date_format)


class LoginError(Exception):
    pass
