from . import WikiBaseTestCase
from wiki.web.UserForm import MyJsonParser
from wiki.web.deleteUser import DeleteJsonParser

class WebContentTestCase(WikiBaseTestCase):
    """
        Various test cases around web content.
    """

    def test_index_missing(self):
        """
            Assert the wiki will correctly play the content missing
            index page, if no index page exists.
        """
        rsp = self.app.get('/')
        assert b"You did not create any content yet." in rsp.data
        assert rsp.status_code == 200

    def test_write_JsonParser(self):
        jsonparser = MyJsonParser()

        assert jsonparser.add_user("name", "1234") is False
        assert jsonparser.add_user("Jesus","1234") is False
        assert jsonparser.add_user("Mark", "Master Of All") is False

    def test_delete_JsonParser(self):
        jsonparser = MyJsonParser()
        DelJsonParser = DeleteJsonParser()

        assert jsonparser.add_user("aaron", "44ron") is True
        assert DelJsonParser.delete_user("aaron") is True