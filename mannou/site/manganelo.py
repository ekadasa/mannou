# -*- coding: utf-8 -*-

"""Manganelo parser.

"""


from .. import parser, util


__all__ = ['Manganelo']


class Manganelo(parser.Manga, domain='manganelo.com'):
    """Parser for https://manganelo.com

    For further details, please read `mannou.parser.Manga` documentation.

    """

    @property
    def _detail_info(self):
        """Helper method used for extracting manga detail.

        """
        return self.soup.select_one('.manga-info-text').select('li')

    @property
    def title(self):
        return self._detail_info[0].h1.text

    @property
    def chapters(self):
        chapter_lists = self.soup.select('.chapter-list > .row')

        chapters = []
        for chapter in reversed(chapter_lists):
            url = chapter.select_one('a')['href']
            number = url.split('/')[-1].replace('chapter_', '')
            chapters.append(parser.Chapter(number, url))

        return chapters

    @staticmethod
    def get_chapter_images(chapter_url):
        soup = util.make_soup(chapter_url)
        image_tags = soup.select_one('#vungdoc').select('img')

        images = []
        for tag in image_tags:
            source = tag['src']
            name = source.split('/')[-1]
            images.append(parser.Image(name, source))

        return images
