# This module handles downloading the tickets and creating Ticket objects for them

import requests

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
    try:
        response = requests.get(url, auth=(user, pwd)) # make a HTTP request
    except requests.exceptions.ConnectionError:
        return False
    # check that the request is valid
    if response.status_code != 200:
        return False
    else:
        return response

def decode_ticket_json(ticket_json):
    # strip a list of dictionaries from the json-string so I can feed them into Ticket objects
    ticket_data = ticket_json.json()
    tickets = ticket_data['tickets'] # select dictionary of tickets
    return tickets

def make_ticket_objects(ticket_dict):
    # make a list of Ticket objects from a list of dictionaries
    ticket_list = []
    for ticket in ticket_dict:
        new_ticket = Ticket(ticket)
        ticket_list.append(new_ticket)
    return ticket_list
