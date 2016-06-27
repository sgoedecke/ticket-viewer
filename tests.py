import unittest
from ticketdownloader import *
from CLIdisplay import *

class DownloaderTestCase(unittest.TestCase):
    #tests for the Ticket downloader module
    def test_single_attribute_assignment(self):
        test_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
        ticket = Ticket(test_dict)
        self.assertTrue(ticket.key2=="value2")
    def test_list_attribute_assignment(self):
        test_dict = {"key1":["value1", "value2"], "key3":"value3"}
        ticket = Ticket(test_dict)
        self.assertTrue(ticket.key1==["value1","value2"])
    #tests for the other functions
    def test_decode_ticket_json(self):
        ticket_json = {"title": "test_ticket", "submitter_id": "0", "id" : "0"}
        ticket = decode_ticket_json(ticket_json)

class CLIDisplayTestCase(unittest.TestCase):
    #tests for the CLI Display module
    def test_display_ticket_list(self):


if __name__ == '__main__':
    unittest.main() #run tests
