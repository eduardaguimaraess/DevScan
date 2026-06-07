import requests


class RequestHandler:

    def fetch(self, url):

        try:
            response = requests.get(url, timeout=5)

            return response

        except requests.RequestException:
            return None