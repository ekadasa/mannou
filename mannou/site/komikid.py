"""Komikid parser.

"""

from .. import util, parser


__all__ = ['Komikid']

def _get_number_from_url(chapter_url):
    number = chapter_url.split('/')[-1]
    if number != '0' or number != '00':
        number = number.lstrip('0')
    return number


class Komikid(parser.Manga, domain='komikid.com'):
    """Parser for http://komikid.com

    For further details, please read `Manga` documentation.

    """

    @property
    def title(self):
        return self.soup.h2.text

    @property
    def chapters(self):
        chapter_lists = self.soup.select('ul.chapters > li')

        chapters = []
        for chapter in reversed(chapter_lists):
            url = chapter.a['href']
            number = _get_number_from_url(url)
            chapters.append(parser.Chapter(number, url))

        return chapters

    @staticmethod
    def get_chapter_images(chapter_url):
        soup = util.make_soup(chapter_url)
        image_tags = soup.select('#all > img')
        for tag in image_tags:
            source = tag['data-src'].strip()
            name = source.split('/')[-1]
            yield parser.Image(name, source)
