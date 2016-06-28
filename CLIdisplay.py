# This module handles the command-line UI

from tabulate import tabulate
import datetime

INPUT_PROMPT = "> "
TICKETS_PER_PAGE = 25

# display functions

def reformat_json_date(date):
    # make the date data more readable
    formatted_date = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
    return formatted_date

def display_ticket_list(ticket_list, start, end):
    # display list of tickets
    print "Viewing tickets from " + str(start) + " to " + str(end) + ":"
    tabulate_list = []
    for ticket in ticket_list[start:end]: #look at first 25 tickets
        tabulate_list.append([ticket.id,ticket.subject,ticket.submitter_id])
    print tabulate(tabulate_list, headers=["ID","Subject","Submitter ID"],tablefmt="simple")
    print "\n"

def display_individual_ticket(ticket):
    formatted_date = reformat_json_date(ticket.created_at)

    print "Subject: " + str(ticket.subject) #using str() here returns "None" if the attribute is missing, rather than throwing an error
    print "Submitter ID: " + str(ticket.submitter_id)
    print "Priority: " + str(ticket.priority)
    print "Status: " + str(ticket.status)
    print "Created at: " + str(formatted_date)
    print "Description: " + str(ticket.description)


# menu functions

def main_menu():
    print "\nSelect view options:"
    print "* Press 1 to view all tickets"
    print "* Press 2 to view a particular ticket"
    print "* Press 3 to exit"
    command = raw_input(INPUT_PROMPT)
    return command

def ticket_list_menu(ticket_list, viewing_from):
    viewing_from = viewing_from

    viewing_list = True
    while viewing_list == True:

        # display tickets
        display_ticket_list(ticket_list, viewing_from, viewing_from+TICKETS_PER_PAGE)
        if viewing_from > 0: # if there are tickets to the left of the viewing set
            tickets_left = True
            print "* Press 1 to view the previous page of tickets"
        else:
            tickets_left = False
        if len(ticket_list) > viewing_from+TICKETS_PER_PAGE: # if there are tickets to the right of the viewing set
            tickets_right = True
            print "* Press 2 to view the next page of tickets"
        else:
            tickets_right = False
        print "* Press 3 to view a particular ticket"
        print "* Press 4 to return to main menu"
        command = raw_input(INPUT_PROMPT)

        # handle user input
        if command == "1" and tickets_left:
            viewing_from = viewing_from-TICKETS_PER_PAGE # go left
        elif command == "2" and tickets_right:
            viewing_from = viewing_from+TICKETS_PER_PAGE # go right
        elif command == "3":
            individual_ticket_menu(ticket_list)
            return
        elif command == "4":
            print "Returning to main menu..."
            return
        else:
            print "Please enter a valid input."


    #can scan forward?
def individual_ticket_menu(ticket_list):
    print "* Enter the ticket id you wish to see."
    command = raw_input(INPUT_PROMPT)
    for ticket in ticket_list:
        if str(ticket.id) == command:
            display_individual_ticket(ticket)
            return
    print "No such ticket."
