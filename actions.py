from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk import Action, Tracker
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Callable, Dict, List, Any, Optional
from schema import schema
import requests
import json

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# KnowledgeBase from Rasa documentation
class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("bank_data.json")

        knowledge_base.set_representation_function_of_object(
            "bank", lambda obj: obj["name"] + " (" + obj["location"] + ")"
        )

        super().__init__(knowledge_base)

    # Overwrite utteractions
    def utter_attribute_value(
            self,
            dispatcher: CollectingDispatcher,
            object_name: Text,
            attribute_name: Text,
            attribute_value: Text,
        ) -> None:
            """
            Utters a response that informs the user about the attribute value of the
            attribute of interest.
            Args:
                dispatcher: the dispatcher
                object_name: the name of the object
                attribute_name: the name of the attribute
                attribute_value: the value of the attribute
            """
            if attribute_value:
                dispatcher.utter_message("Það er opið frá {} í {}.".format(attribute_value, object_name))
            else:
                dispatcher.utter_message("Það fannst enginn opnunartími í {}.".format(object_name))

    def utter_objects(
            self,
            dispatcher: CollectingDispatcher,
            object_type: Text,
            objects: List[Dict[Text, Any]],
        ) -> None:
            """
            Utters a response to the user that lists all found objects.
            Args:
                dispatcher: the dispatcher
                object_type: the object type
                objects: the list of objects
            """
          
            if objects:
                if (len(objects)==25):
                    dispatcher.utter_message("Það voru margar niðurstöður, hérna koma fyrstu 25")
                else:
                    dispatcher.utter_message("Hér eru niðurstöðurnar:")

                repr_function = self.knowledge_base.get_representation_function_of_object(object_type)

                for i, obj in enumerate(objects, 1):
                    dispatcher.utter_message("{}: {}".format(i, repr_function(obj)))
            else:
                dispatcher.utter_message("Fyrirgefðu ég fann enga {} á þessu svæði.".format(object_type))

# Action to query exchange rate
class ActionExchangeRate(Action):

    def name(self) -> Text:
        return "action_query_exchange_rate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Get entities from nlu.md
        rate = tracker.get_slot('rate')
        base = tracker.get_slot('base')
        amount = next(tracker.get_latest_entity_values('amount'), None)

        URL = 'https://api.exchangeratesapi.io/latest'

        if base is not None:
            r = requests.get(URL + '?base=' + base)
        else:
            r = requests.get(URL + '?base=ISK')

        response = r.text
        json_data = json.loads(response)
        rates = json.loads(response)['rates']

        # Check which entities are in user query
        if rate is not None and base is not None and amount is not None:
            rate = rate.upper()
            # Check if rate value and base value exist in api and convert
            if rates[rate] is not None and json_data['base'] is not None:
                result = float(rates[rate]) * float(amount)
                result = round(result,2)
                dispatcher.utter_message("{} {} eru {} {}".format(amount, base, result, rate))
            else:
                dispatcher.utter_message("Fannst ekki í gögnum")
        elif rate is not None and base is None and amount is None:
            if rates[rate] is not None:
                dispatcher.utter_message("Gengið í {} er {} miðað við {}".format(rate, rates[rate], json_data['base']))
            else:
                dispatcher.utter_message("Fannst ekki í gögnum")
        else:
            dispatcher.utter_message("404 fannst ekki")

        return []

# Action to get random Chuck Norris jokes
class ActionChuckNorris(Action):

    def name(self) -> Text:
        return "action_query_chuck_norris"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        r = requests.get('https://api.chucknorris.io/jokes/random')
        response = r.text
        jokes = json.loads(response)

        if (jokes["value"]):
            reply = jokes["value"]
            dispatcher.utter_message("Hér er brandarinn: \n {}".format(reply))
        else:
            dispatcher.utter_message("Ég er ekki fyndinn.")

        return []
