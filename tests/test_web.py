from . import WikiBaseTestCase
from wiki.web import UserForm

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
        jsonparser = UserForm.MyJsonParser

        assert jsonparser.add_user("name","1234") is False