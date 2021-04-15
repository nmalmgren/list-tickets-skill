from mycroft import MycroftSkill, intent_file_handler
import sqlite3
from sqlite3 import Error


class ListTickets(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tickets.list.intent')
    def handle_tickets_list(self, message):
        database1 = "cubic.sql"

        # create a database connection
        conn = sqlite3.connect(database1)
        cur = conn.cursor()
    
        cur.execute("SELECT * FROM PassData")
        rows = cur.fetchall()
        i=1
        self.speak('Here are the available tickets.')
        for row in rows:
            cur.execute("SELECT * FROM TransitLine WHERE LineID = ?", (row[3],))
            idrow = cur.fetchone()
            self.speak('Ticket {} starts at {}, ends at {}, has an E.T.A of {}, and costs {}.'.format(i, row[4], row[5], idrow[3], row[6]))
            i += 1
        conn.close()


def create_skill():
    return ListTickets()
