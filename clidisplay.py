# This module handles the command-line UI
from tabulate import tabulate
import datetime

INPUT_PROMPT = "> "
TICKETS_PER_PAGE = 25


def reformat_json_date(date):
    # make the date data more readable
    formatted_date = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
    return formatted_date

# display functions

def display_ticket_list(ticket_list, start, end):
    # display list of tickets
    if end > len(ticket_list):
        end = len(ticket_list)
    print "Viewing tickets from " + str(start) + " to " + str(end) + " (out of " + str(len(ticket_list)) + " total):"
    tabulated_list = []
    for ticket in ticket_list[start:end]: #look at first 25 tickets
        tabulated_list.append([ticket.id,ticket.subject,ticket.submitter_id, reformat_json_date(ticket.created_at)])
    print tabulate(tabulated_list, headers=["ID","Subject","Submitter ID", "Submitted at"],tablefmt="simple") + "\n"

def display_individual_ticket(ticket):
    # display details for a single ticket
    formatted_date = reformat_json_date(ticket.created_at)
    print "\nViewing ticket with ID: " + str(ticket.id)
    print "Subject: " + str(ticket.subject) #using str() here returns "None" if the attribute is missing, rather than throwing an error
    print "Submitter ID: " + str(ticket.submitter_id)
    print "Priority: " + str(ticket.priority)
    print "Status: " + str(ticket.status)
    print "Created at: " + str(formatted_date)
    print "Description: " + str(ticket.description) + "\n"

def display_main():
    # display the main menu
    print "Select view options:"
    print "* Press 1 to view all tickets"
    print "* Press 2 to view a particular ticket"
    print "* Press 3 to exit"

# menu functions

def main_menu(ticket_list):
    # handle input for the main menu
    ticket_list = ticket_list

    viewing = True
    while viewing == True:
        display_main()
        command = raw_input(INPUT_PROMPT)
        if command == "1":
            ticket_list_menu(ticket_list, 0) # start viewing from first ticket
        elif command == "2":
            individual_ticket_menu(ticket_list)
        elif command == "3":
            return # exit program
        else:
            print "Please enter a valid input."

def ticket_list_menu(ticket_list, viewing_from):
    # handle input while displaying a list of tickets
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

def individual_ticket_menu(ticket_list):
    # handle input while displaying individual tickets
    print "* Enter the ticket id you wish to see."
    command = raw_input(INPUT_PROMPT)
    for ticket in ticket_list:
        if str(ticket.id) == command:
            display_individual_ticket(ticket)
            return
    print "No such ticket."
