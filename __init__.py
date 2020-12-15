from mycroft import MycroftSkill, intent_file_handler


class CalorieLookup(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lookup.calorie.intent')
    def handle_lookup_calorie(self, message):
        self.speak_dialog('lookup.calorie')


def create_skill():
    return CalorieLookup()

