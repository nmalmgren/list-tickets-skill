from mycroft import MycroftSkill, intent_file_handler


class ListTickets(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tickets.list.intent')
    def handle_tickets_list(self, message):
        self.speak_dialog('tickets.list')


def create_skill():
    return ListTickets()

