import requests
import json

#this code is mostly ripped off the zendesk site.


##### Classes ####
class Ticket:
    def __init__(self, dict):
        for key,value in dict.items():
            if isinstance(value, (list, tuple)): #if the property's a list (or tuple), assign it a list here too
                setattr(self, key, [x for x in value])
            else:
                setattr(self, key,  value)

#### Functions ####

def get_ticket_json(url, auth=(user,pwd)):
    #make a HTTP request
    response = requests.get(url, auth=(user, pwd))
    #check that the request is valid
    if response.status_code != 200:
        return False
    else:
        return response

def decode_ticket_json(ticket_json):
    ticket_data = ticket_json.json()
    tickets = ticket_data['tickets'] #select list of tickets from the dictionary
    return tickets


#### Main loop ####

#Get the url, username and password

url = "https://sgoedecke.zendesk.com/api/v2/tickets.json"
user = "sean.goedecke@gmail.com"
pwd = "Porcup1n"

#Get the list of tickets

response = get_ticket_json(url,auth=(user,pwd))

#check if the response is throwing an error
if response == False:
    print "Error!"
else:
    tickets = decode_ticket_json(response)

#Display list of tickets

for ticket in ticket_list[:24]: #look at first 25 tickets
    new_ticket = Ticket(ticket)
    print new_ticket.id
    print new_ticket.subject
    print new_ticket.created_at
    print new_ticket.updated_at
#    new_ticket = Ticket(id=ticket['id'],subject=ticket['subject'])
#    print new_ticket
#    print new_ticket.id
#    print new_ticket.subject


'''
try:
    print str(ticket_list[0]['id'])
except:
    print "No id!"

try:
    print str(ticket_list[0]['url'])
except:
    print "No url!"

try:
    print str(ticket_list[0]['type'])
except:
    print "No type!"

try:
    print str(ticket_list[0]['subject'])
except:
    print "No subject!"

try:
    print str(ticket_list[0]['description'])
except:
    print "No description!"
    '''
