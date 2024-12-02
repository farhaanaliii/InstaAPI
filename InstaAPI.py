import requests
from typing import List

class InstaPost:
    def __init__(self, thumbnail: str, download: str):
        self.thumbnail = thumbnail
        self.download = download

    def __repr__(self):
        return f"InstaPost(thumbnail='{self.thumbnail}', download='{self.download}')"

class InstaAPI:
    """
    A Python Wrapper for Instagram Downloader API on RapidAPI.
    """

    BASE_URL = "https://test-api646.p.rapidapi.com/"

    def __init__(self, key: str):
        """
        Initializes the InstaAPI client. 🛠️

        :param key: Your RapidAPI key.
        """
        if not key:
            raise ValueError("API key is required! 😢")
        
        self.key = key
        self.headers = {
            "X-RapidAPI-Key": self.key,
            "X-RapidAPI-Host": "test-api646.p.rapidapi.com"
        }

    def get_links(self, url: str) -> List[InstaPost]:
        """
        Fetches links for an Instagram post. 🖼️

        :param url: The Instagram post URL.
        :return: A list of InstaPost objects.
        :raises Exception: If the API call fails.
        """
        params = {"url": url}
        try:
            res = requests.get(self.BASE_URL, headers=self.headers, params=params)
            res.raise_for_status()
            data = res.json()

            if data.get("status") != "success":
                raise ValueError(f"API Error: {data.get('message', 'No details provided 😕')}")

            posts = [
                InstaPost(item["thumbnail"], item["download"])
                for item in data.get("data", [])
            ]

            return posts
        except requests.exceptions.RequestException as err:
            raise Exception(f"Request failed: {err} 🚨")
        except ValueError as err:
            raise Exception(f"API Error: {err} 🚫")

    def __repr__(self):
        return f"<InstaAPI(host={self.headers['X-RapidAPI-Host']})>"
