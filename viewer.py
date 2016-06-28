from tickethandler import *
from clidisplay import *


# authentication info
url = "https://sgoedecke.zendesk.com/api/v2/tickets.json"
user = "sean.goedecke@gmail.com"
pwd = "Porcup1n"

def run_ticket_viewer():
    # download the tickets and build a Ticket object for each ticket
    print "Welcome to the ticket viewer! \n"

    has_tickets = False
    while has_tickets == False:
        # get the list of tickets
        print "Downloading tickets from '" + url + "..."
        response = get_ticket_json(url,user,pwd)

        # check if the response is throwing an error
        if response == False:
            print "Could not access tickets. Make sure you are connected to the internet."
            return # exit program
        else:
            tickets_dict = decode_ticket_json(response)
            ticket_list = make_ticket_objects(tickets_dict)
            print "Successfully downloaded " + str(len(ticket_list)) + " tickets."
            has_tickets = True

    # let the user view the downloaded tickets
    viewing = True
    while viewing == True:
        command = main_menu() # display main menu
        if command == "1":
            ticket_list_menu(ticket_list, 0) # start viewing from first ticket
        elif command == "2":
            individual_ticket_menu(ticket_list)
        elif command == "3":
            return # exit program
        else:
            print "Please enter a valid input."


if __name__ == '__main__':
    try:
        run_ticket_viewer()
    except KeyboardInterrupt: # exit gracefully if user presses Ctrl+C
        pass
    finally:
        print "\nThank you for using the ticket viewer."
