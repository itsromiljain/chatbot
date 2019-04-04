from rasa_core_sdk import Action
import requests
import json


class ActionGetNewst(Action):

    def name(self):
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        url = 'https://api.nytimes.com/svc/news/v3/content/all/{category}.json'.format(category=category)
        params = {'api-key': "YwFANMbVPDGGaM7aNgXuPdlkt2DuEK6I", 'limit': 5}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return[]
