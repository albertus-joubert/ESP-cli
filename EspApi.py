import requests

URL = "https://developer.sepush.co.za/business/2.0/"
class EspApi:
    def __init__(self, token):
        self.token = token

    def status(self):
        return requests.get(
            URL + "status",
            headers={"token": self.token}
        ).json()

    def area_test(self, id, test):
        return requests.get(
            URL + "area?id=" + id + "&test=" + test,
            headers={"token": self.token}
        ).json()

    def area(self, id):
        return requests.get(
            URL + "area?id=" + id,
            headers={"token": self.token}
        ).json()

    def areas_nearby(self, lat, lon):
        return requests.get(
            URL + "areas_nearby?lat=" + str(lat) + "&lon" + str(lon),
            headers={"token": self.token}
        ).json()

    def areas_search(self, text):
        return requests.get(
            URL + "areas_search?text=" + text,
            headers={"token": self.token}
        ).json()

    def topics_nearby(self, lat, lon):
        return requests.get(
            URL + "topics_nearby?lat=" + str(lat) + "&lon=" + str(lon),
            headers={"token": self.token}
        ).json()

    def check_allowance(self):
        return requests.get(
            URL + "api_allowance",
            headers={"token": self.token}
        ).json();
