from unittest import TestCase

from redux.site.mangapanda import MangaPanda


class TestMangaPanda(TestCase):
    SERIES = MangaPanda.series('gantz')
    CHAPTERS = SERIES.chapters

    def test_chapter_count(self):
        self.assertEqual(len(TestMangaPanda.SERIES.chapters), 383)

    def test_chapter_title(self):
        self.assertEqual(TestMangaPanda.CHAPTERS[-2].title, 'Lightning Counterstrike')

    def test_chapter_pages(self):
        self.assertEqual(len(TestMangaPanda.CHAPTERS[0].pages), 43)