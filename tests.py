import unittest
from tickethandler import *
from clidisplay import *

class DummyResponseObject:
    # this mimicks a Response object from the Requests library, for easier testing
    def __init__(self,dummy_json):
        self.dummy_json = dummy_json
    def json(self):
        return self.dummy_json

class TicketObjectTestCase(unittest.TestCase):
    # tests for the Ticket object
    def test_Ticket_attribute_assignment(self):
        test_dict = {"key1":"value1", "key2":"value2", "key3":"value3"}
        ticket = Ticket(test_dict)
        self.assertTrue(ticket.key2=="value2")
    def test_Ticket_list_attribute_assignment(self):
        test_dict = {"key1":["value1", "value2"], "key3":"value3"}
        ticket = Ticket(test_dict)
        self.assertTrue(ticket.key1==["value1","value2"])

class TicketHandlerTestCase(unittest.TestCase):
    # tests for the ticket handling methods
    def test_decode_ticket_json(self):
        ticket_json = DummyResponseObject({"tickets":{"title": "test_ticket", "submitter_id": "0", "id" : "0"}})
        ticket = decode_ticket_json(ticket_json)
        self.assertTrue(ticket == {"title":"test_ticket","submitter_id":"0","id":"0"})
    def test_make_ticket_objects(self):
        ticket_dict = [{"title":"test_ticket","submitter_id":"0","id":"0"}]
        ticket_list = make_ticket_objects(ticket_dict, [])
        my_ticket = ticket_list[0]
        self.assertTrue(my_ticket.title == "test_ticket")

class CLIDisplayTestCase(unittest.TestCase):
    # tests for the CLI Display module
    def test_reformat_json_date(self):
        raw_date = '2012-05-29T18:29:10Z'
        formatted_date = reformat_json_date(raw_date)
        self.assertTrue(str(formatted_date) == '2012-05-29 18:29:10')


if __name__ == '__main__':
    unittest.main() #run tests
