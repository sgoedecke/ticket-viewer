import unittest
import mock
from tickethandler import *
from clidisplay import *

## Tests for the tickethandler.py module below:

class DummyResponseObject:
    # this mimicks a Response object from the Requests library, for easier testing
    def __init__(self,dummy_json):
        self.dummy_json = dummy_json
    def json(self):
        return self.dummy_json
def test_requests_get_one_page(url, auth):
    # mimicks the requests.get without actually making a HTTP request
    dummy_json = {"next_page": None, "tickets":{"title": "test_ticket", "id" : "0"}}
    dummy_response = DummyResponseObject(dummy_json)
    dummy_response.status_code = 200
    return dummy_response
def test_requests_get_two_pages(url, auth):
    if url != "next_page_url": # if this function's being run for the first time
        dummy_json = {"next_page": "next_page_url", "tickets":{"title": "test_ticket", "id" : "0"}}
    else:
        dummy_json = {"next_page": None, "tickets":{"title": "test_ticket", "id" : "0"}}
    dummy_response = DummyResponseObject(dummy_json)
    dummy_response.status_code = 200
    return dummy_response
def test_requests_get_bad_status_code(url, auth):
    dummy_json = {"next_page": None, "tickets":{"title": "test_ticket", "id" : "0"}}
    dummy_response = DummyResponseObject(dummy_json)
    dummy_response.status_code = 100
    return dummy_response

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

    @mock.patch('requests.get', side_effect=test_requests_get_one_page) # replace requests.get with my dummy function to avoid making a HTTP request
    def test_get_ticket_json_one_page(self, test_get):
        response_list = get_ticket_json("url","user","pwd")
        self.assertTrue(len(response_list)==1)
    @mock.patch('requests.get', side_effect=test_requests_get_two_pages)
    def test_get_ticket_json_two_pages(self, test_get):
        response_list = get_ticket_json("url","user","pwd")
        self.assertTrue(len(response_list)==2)
    @mock.patch('requests.get', side_effect=test_requests_get_bad_status_code)
    def test_get_ticket_json_bad_status_code(self, test_get):
        response_list = get_ticket_json("url","user","pwd")
        self.assertTrue(response_list == False)

## Tests for the clidisplay.py module below:

class CLIDisplayTestCase(unittest.TestCase):
    # tests for the methods in clidisplay
    def test_reformat_json_date(self):
        raw_date = '2012-05-29T18:29:10Z'
        formatted_date = reformat_json_date(raw_date)
        self.assertTrue(str(formatted_date) == '2012-05-29 18:29:10')


if __name__ == '__main__':
    unittest.main() #run tests
