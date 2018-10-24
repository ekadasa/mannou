"""Main Test for ``mannou.anilist``

"""

from mannou import anilist
import json

CUSTOM_QUERY = """
query ($name: String) {
    Media(search: $name, type: MANGA) {
        isAdult
        type
    }
}
"""

def test_anilist():
    title = 'Tomo-chan wa Onnanoko!'
    manga = anilist.AniList(title)
    info = manga.info()
    assert info['id'] == 86300

    manga.query = CUSTOM_QUERY
    info = manga.info()
    assert info['type'] == 'MANGA'
