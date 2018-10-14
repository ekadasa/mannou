# -*- coding: utf-8 -*-

import json

import requests


API_URL = 'https://graphql.anilist.co'

QUERY = """
query ($name: String) {
    Media (search: $name, type: MANGA) {
        id
        idMal
        title {
            romaji
            english
            native
            userPreferred
        }
        genres
        description
        siteUrl
    }
}
"""

class MangaInfo:

    def __init__(self, name):
        self.name = name

    def json(self):
        data = {
            'query': QUERY,
            'variables': {
                'name': self.name
            }
        }
        response = requests.post(API_URL, json=data)
        return response

    def info(self):
        response = self.json()
        load_data = json.loads(response.text)
        return load_data['data']['Media']
