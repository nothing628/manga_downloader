from unittest import TestCase

from redux.site.mangareader import MangaReader


class MangaReader(TestCase):
    SERIES = MangaReader.series('gantz')
    CHAPTERS = SERIES.chapters

    def test_chapter_count(self):
        self.assertEqual(len(MangaReader.SERIES.chapters), 383)

    def test_chapter_title(self):
        self.assertEqual(MangaReader.CHAPTERS[-2].title, 'Lightning Counterstrike')

    def test_chapter_pages(self):
        self.assertEqual(len(MangaReader.CHAPTERS[0].pages), 43)