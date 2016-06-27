#This module handles the command-line UI

INPUT_PROMPT = "~: "
TICKETS_PER_PAGE = 25

def main_menu():
    print "Select view options:"
    print "* Press 1 to view all tickets"
    print "* Press 2 to view a particular ticket"
    command = raw_input(INPUT_PROMPT)
    return command

def display_ticket_list(ticket_list, start, end):
    #display list of tickets
    print "Viewing tickets from " + str(start) + " to " + str(end)
    for ticket in ticket_list[start:end]: #look at first 25 tickets
        print str(ticket.id) + " with subject: " + str(ticket.subject)

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
            print str(ticket.id) + " with subject " + str(ticket.subject)
            #what if invalid ticket?

#authentication functions for login menu

def is_valid_url_name(url):
    #test if string is a valid Zendesk username
    return True

def is_valid_email(email):
    return True

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
