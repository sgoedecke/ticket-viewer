#This module handles the command-line UI

from tabulate import tabulate
import datetime
import re

INPUT_PROMPT = "~: "
TICKETS_PER_PAGE = 25

# input validation functions for login menu

def has_no_whitespace(text):
    #return True if string has no whitespace
    if re.search(r"\s",text):
        return False
    else:
        return True

def is_valid_email(email):
    #return True if string looks like a valid email (i.e. has only one '@', with some stuff on either side, and ends with dot-something)
    if re.match(r"[^@]+@[^@]+\.[^@]+",email) and has_no_whitespace(email):
        return True
    else:
        return False

# display functions

def reformat_json_date(date):
    #makes the date data more readable
    formatted_date = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
    return formatted_date

def display_ticket_list(ticket_list, start, end):
    #display list of tickets
    print "Viewing tickets from " + str(start) + " to " + str(end)
    tabulate_list = []
    for ticket in ticket_list[start:end]: #look at first 25 tickets
        tabulate_list.append([ticket.id,ticket.subject,ticket.submitter_id])
    print tabulate(tabulate_list, headers=["ID","Subject","Submitter ID"],tablefmt="simple")

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
    print "Select view options:"
    print "* Press 1 to view all tickets"
    print "* Press 2 to view a particular ticket"
    print "* Press 3 to exit"
    command = raw_input(INPUT_PROMPT)
    return command

def ticket_list_menu(ticket_list, viewing_from):
    viewing_from = viewing_from

    viewing_list = True
    while viewing_list == True:

        #display tickets
        display_ticket_list(ticket_list, viewing_from, viewing_from+TICKETS_PER_PAGE)
        if viewing_from > 0: #if there are tickets to the left of the viewing set
            tickets_left = True
            print "* Press 1 to view earlier tickets"
        else:
            tickets_left = False
        if len(ticket_list) > viewing_from+TICKETS_PER_PAGE: #if there are tickets to the right of the viewing set
            tickets_right = True
            print "* Press 2 to view later tickets"
        else:
            tickets_right = False
        print "* Press 3 to view a particular ticket"
        print "* Press 4 to return to main menu"
        command = raw_input(INPUT_PROMPT)

        #handle user input
        if command == "1" and tickets_left:
            #go left
            viewing_from = viewing_from-TICKETS_PER_PAGE
        elif command == "2" and tickets_right:
            #go right
            viewing_from = viewing_from+TICKETS_PER_PAGE
        elif command == "3":
            viewing_list = False
            individual_ticket_menu(ticket_list)
        elif command == "4":
            print "Returning to main menu..."
            viewing_list = False
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

def login_menu():
    print "Welcome to the ticket viewer."
    print "Log in with your Zendesk account details."

    has_url = False
    while has_url == False:
        print "Enter your Zendesk username (the one in your url):"
        url_name = raw_input(INPUT_PROMPT)
        if has_no_whitespace(url_name): #minimal check for valid username
            has_url = True
        else:
            print "Sorry, this is an invalid username."
    url = "https://" + url_name + ".zendesk.com/api/v2/tickets.json"

    has_email = False
    while has_email == False:
        print "Enter the email you signed up to Zendesk with:"
        user = raw_input(INPUT_PROMPT)
        if is_valid_email(user):
            has_email = True
        else:
            print "Sorry, this is an invalid email."


    print "Enter your password:"
    pwd = raw_input(INPUT_PROMPT) #TODO - make this a proper password input

    return [url, user, pwd]
