# This module handles downloading the tickets and creating Ticket objects for them
import requests
import time

class Ticket:
    # ticket objects read their attributes straight from the .json
    def __init__(self, dict):
        for key,value in dict.items():
            if isinstance(value, (list, tuple)): # check if the ticket property is a list (e.g. a list of tags)
                setattr(self, key, [x for x in value])
            else:
                setattr(self, key,  value)

def get_ticket_json(url, user,pwd):
    # get the ticket information using the Zendesk API
    response_list = []
    try:
        while url: # need to check for multiple pages of results
            response = requests.get(url, auth=(user, pwd)) # make a HTTP request
            if response.status_code == 429: # handle hitting the rate limit
                print "Rate limited. Waiting..."
                response_dict = response.json()
                time_to_wait = response_dict['retry-after']
                time.sleep(int(time_to_wait))
                continue
            elif response.status_code != 200:
                return False
            else:
                response_list.append(response)
                response_dict = response.json()
                url = response_dict['next_page']
                if url:
                    print "Getting next page of tickets..."

    except requests.exceptions.ConnectionError:
        return False
    # check that the request is valid
    return response_list


def decode_ticket_json(ticket_json):
    # strip a list of dictionaries from the json-string so I can feed them into Ticket objects
    ticket_data = ticket_json.json()
    tickets = ticket_data['tickets'] # select the tickets
    return tickets

def make_ticket_objects(ticket_dict, ticket_list):
    # make a list of Ticket objects from a list of dictionaries
    for ticket in ticket_dict:
        new_ticket = Ticket(ticket)
        ticket_list.append(new_ticket)
    return ticket_list
