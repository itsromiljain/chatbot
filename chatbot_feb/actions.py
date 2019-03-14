from rasa_core_sdk import Action


class ActionCreateTicket(Action):

    def name(self):
        return 'action_create_ticket'

    def run(self, dispatcher, tracker, domain):
        devicename = tracker.get_slot('device_name')
        modelname = tracker.get_slot('model_name')
        ticketnumber = 123456  # will call the API
        response = """Here are the details of your ticket {} for Device {} and Model {}""".format(ticketnumber, devicename, modelname)
        dispatcher.utter_message(response)
        return[]
