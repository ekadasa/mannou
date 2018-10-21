# -*- coding: utf-8 -*-

"""Interraction module to AniList API.

See Also
--------
`mannou.api` : An implementation of this module.

.. _AniList API documentation:
    https://anilist.gitbook.io/anilist-apiv2-docs

"""


import json

import requests


__all__ = ['API_URL', 'QUERY', 'AniList']

API_URL = 'https://graphql.anilist.co'
"""AniList GraphQL API.

"""

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
"""Default query that sent to AniList API.

"""


class AniList:
    """Main class to communicate with AniList API.

    Attributes
    ----------
    api_url : str
        AniList API url
    query : str
        Query that you want to sent to. It must be GraphQL query and
        exists in AniList API.

    Parameters
    ----------
    name : str
        Name of the manga that you want to get.

    """

    api_url = API_URL
    query = QUERY

    def __init__(self, name):
        self.name = name

    def json(self):
        """Get response in JSON format.

        Returns
        -------
        str
            Response from API server in JSON format.

        """
        data = {
            'query': self.query,
            'variables': {
                'name': self.name
            }
        }
        response = requests.post(self.api_url, json=data)
        return response

    def info(self):
        """Get response in dictionary.

        Returns
        -------
        dict
            Parsed response from `self.json`.

        """
        response = self.json()
        load_data = json.loads(response.text)
        return load_data['data']['Media']
