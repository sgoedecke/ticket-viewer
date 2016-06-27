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
        ticket_json = {"title": "test_ticket", "submitter_id": "0", "id" : "0"}
        ticket = decode_ticket_json(ticket_json)
        # THIS IS RETURNING 'ERROR'

class CLIDisplayTestCase(unittest.TestCase):
    #tests for the CLI Display module
    def test_is_valid_url_name_recognising_valid_email(self):
        url_name = "validname"
        is_valid = is_valid_url_name(url_name)
        self.assertTrue(is_valid)

    def test_is_valid_url_name_recognising_invalid_email(self):
        url_name = "not a valid name"
        is_valid = is_valid_url_name(url_name)
        self.assertFalse(is_valid)

    def test_is_valid_email_recognising_valid_email(self):
        email = "valid@email.com"
        is_valid = is_valid_email(email)
        self.assertTrue(is_valid)

    def test_is_valid_email_recognising_invalid_email(self):
        email = "this isn't a valid email"
        is_valid = is_valid_email(email)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main() #run tests
