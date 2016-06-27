# This module handles downloading the tickets and

import requests
import json


##### Classes ####
class Ticket:
    #basic Ticket class, with attributes straight from the .json
    def __init__(self, dict):
        for key,value in dict.items():
            if isinstance(value, (list, tuple)): #if the property's a list (or tuple), assign it a list here too
                setattr(self, key, [x for x in value])
            else:
                setattr(self, key,  value)

#### Functions ####

def get_ticket_json(url, user,pwd):
    #gets the json-format string from the Zendesk API
    #make a HTTP request
    response = requests.get(url, auth=(user, pwd))
    #check that the request is valid
    if response.status_code != 200:
        return False
    else:
        return response

def decode_ticket_json(ticket_json):
    #strips a list of dictionaries from the json-string so I can feed them into Ticket objects
    ticket_data = ticket_json.json()
    tickets = ticket_data['tickets'] #select list of tickets from the dictionary
    return tickets

def make_ticket_objects(ticket_dict):
    #make Ticket objects
    ticket_list = []
    for ticket in ticket_dict:
        new_ticket = Ticket(ticket)
        ticket_list.append(new_ticket)
    return ticket_list
