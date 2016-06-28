import unittest
from tickethandler import *
from clidisplay import *

class HandlerTestCase(unittest.TestCase):
    #tests for the Ticket handler module
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
        ticket_json = json.dumps({"title": "test_ticket", "submitter_id": "0", "id" : "0"})
        ticket = decode_ticket_json(ticket_json)
        # THIS IS RETURNING 'ERROR'

class CLIDisplayTestCase(unittest.TestCase):
    #tests for the CLI Display module


    def test_reformat_json_date(self):
        raw_date = '2012-05-29T18:29:10Z'
        formatted_date = reformat_json_date(raw_date)
        self.assertTrue(str(formatted_date) == '2012-05-29 18:29:10')


if __name__ == '__main__':
    unittest.main() #run tests
