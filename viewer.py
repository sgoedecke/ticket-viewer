from ticketdownloader import *
from CLIdisplay import *


'''
url = "https://sgoedecke.zendesk.com/api/v2/tickets.json"
user = "sean.goedecke@gmail.com"
pwd = "Porcup1n"
'''

#Login the user, download the tickets, and build a Ticket object for each ticket

has_tickets = False
while has_tickets == False:
    #Get the url, username and password
    auth_info = login_menu()
    url = auth_info[0]
    user = auth_info[1]
    pwd = auth_info[2]

    #Get the list of tickets
    print "Trying to download tickets from " + url + " for user " + user
    response = get_ticket_json(url,user,pwd)
    #check if the response is throwing an error
    if response == False: #TODO extend
        print "Could not download tickets."
        continue
    else:
        tickets_dict = decode_ticket_json(response)
        has_tickets = True
        ticket_list = make_ticket_objects(tickets_dict)

#Let the user view the downloaded tickets

viewing = True
while viewing == True:
    #menu
    command = main_menu()

    if command == "1":
        ticket_list_menu(ticket_list, 0) #start viewing from first ticket
    elif command == "2":
        individual_ticket_menu(ticket_list)
    else:
        print "Please enter a valid input."
        continue
