from tickethandler import *
from clidisplay import *


'''
url = "https://sgoedecke.zendesk.com/api/v2/tickets.json"
user = "sean.goedecke@gmail.com"
pwd = "Porcup1n"
'''
def run_ticket_viewer():
    #Login the user, download the tickets, and build a Ticket object for each ticket

    has_tickets = False
    while has_tickets == False:
        #Get the url, username and password
        auth_info = login_menu()
        url = auth_info[0]
        user = auth_info[1]
        pwd = auth_info[2]

        #Get the list of tickets
        print "Trying to download tickets from '" + url + "' for user " + user + "..."
        response = get_ticket_json(url,user,pwd)

        #check if the response is throwing an error
        if response == False:
            print "Could not access tickets. Make sure your user data is correct and you are connected to the internet."
            continue
        else:
            tickets_dict = decode_ticket_json(response)
            ticket_list = make_ticket_objects(tickets_dict)
            print "Downloaded " + str(len(ticket_list)) + " tickets. \n"
            has_tickets = True

    #Let the user view the downloaded tickets

    viewing = True
    while viewing == True:
        #menu
        command = main_menu()

        if command == "1":
            ticket_list_menu(ticket_list, 0) #start viewing from first ticket
        elif command == "2":
            individual_ticket_menu(ticket_list)
        elif command == "3":
            break #exit program
        else:
            print "Please enter a valid input."
            continue

if __name__ == '__main__':
    try:
        run_ticket_viewer()
    except KeyboardInterrupt: #Exit gracefully if user presses Ctrl+C
        pass
    finally:
        print "\nThank you for using the ticket viewer."
