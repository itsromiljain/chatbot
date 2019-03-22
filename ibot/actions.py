from rasa_core_sdk import Action
import requests


class ActionCreateTicket(Action):

    def name(self):
        return 'action_create_ticket'

    def run(self, dispatcher, tracker, domain):
        devicename = tracker.get_slot('device_name')
        modelname = tracker.get_slot('model_name')
        ticketDescription = "Screen is Damaged"
        task = {"deviceName": devicename, "modelName": modelname, "ticketDescription": ticketDescription}
        response = requests.post('http://localhost:7020/dstracker/rest/v1/ticket', json=task)
        ticketnumber = response.text
        print(ticketnumber)
        response = """Here are the details of your ticket {} for Device {} and Model {}""".format(ticketnumber, devicename, modelname)
        dispatcher.utter_message(response)
        return[]
