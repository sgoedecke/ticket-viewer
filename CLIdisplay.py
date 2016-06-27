#This module handles the command-line UI
from tabulate import tabulate
import datetime

INPUT_PROMPT = "~: "
TICKETS_PER_PAGE = 25

# authentication functions for login menu

def is_valid_url_name(url):
    #test if string is a valid Zendesk username
    return True

def is_valid_email(email):
    #test if string is a valid email
    return True

# display functions

def reformat_json_date(date):
    formatted_date = datetime.datetime.strptime(date,'%Y-%m-%dT%H:%M:%SZ')
    return formatted_date

def display_ticket_list(ticket_list, start, end):
    #display list of tickets
    print "Viewing tickets from " + str(start) + " to " + str(end)
    tabulate_list = []
    for ticket in ticket_list[start:end]: #look at first 25 tickets
        tabulate_list.append([ticket.id,ticket.subject,ticket.submitter_id])
    print tabulate(tabulate_list, headers=["ID","Subject","Submitter ID"],tablefmt="fancy_grid")
#        print str(ticket.id) + " with subject: " + str(ticket.subject)

def display_individual_ticket(ticket):
    formatted_date = reformat_json_date(ticket.created_at)
    tabulate_list = [["Subject:",ticket.subject],["Submitter ID:",ticket.submitter_id],["Priority:",ticket.priority],["Status:",ticket.status],["Created at:",formatted_date]]
#    headers = ["ID","Subject","Submitter ID","Description","Priority","Status","Date created"]
    print tabulate(tabulate_list,tablefmt="fancy_grid")
    print "Description: " + ticket.description
#    print str(ticket.id) + " with subject " + str(ticket.subject)

# menu functions

def main_menu():
    print "Select view options:"
    print "* Press 1 to view all tickets"
    print "* Press 2 to view a particular ticket"
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
        print "* Press 3 to return to main menu"
        command = raw_input(INPUT_PROMPT)

        #handle user input
        if command == "1" and tickets_left:
            #go left
            viewing_from = viewing_from-TICKETS_PER_PAGE
        elif command == "2" and tickets_right:
            #go right
            viewing_from = viewing_from+TICKETS_PER_PAGE
        elif command == "3":
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
            #what if invalid ticket?

def login_menu():
    print "Welcome to the ticket viewer."
    print "Log in with your Zendesk account details."

    has_url = False
    while has_url == False:
        print "Enter your Zendesk username (the one in your url):"
        url_name = raw_input(INPUT_PROMPT)
        if is_valid_url_name(url_name):
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
