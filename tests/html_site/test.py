import os
from rucola import Rucola
from tests import FunctionalTest

class Test(FunctionalTest):

    def test(self):

        app = Rucola(os.path.dirname(__file__))

        for page in app.find('*.html'):
            if page.path != 'index.html':
                root, ext = os.path.splitext(page.path)
                page.path = root + '/' + 'index.html'

        app.build()

        self.compare(app)


    # def test_plugin(self):
    #
    #     def ext(app):
    #         for page in app.find('*.html'):
    #             if page.path != 'index.html':
    #                 root, ext = os.path.splitext(page.path)
    #                 page.path = root + '/' + 'index.html'
    #
    #
    #
    #
    #     self.compare(
    #         Rucola(os.path.dirname(__file__)).use(ext).build()
    #     )