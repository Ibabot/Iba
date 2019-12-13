from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk import Action, Tracker
from rasa_sdk.events import FollowupAction, ConversationPaused, ConversationResumed, SlotSet
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Callable, Dict, List, Any, Optional
from rasa.core.slots import Slot
import requests
import json
import pandas as pd

#find nearest location based on coordinates to use in nearest bank
from math import cos, sqrt
#https://stackoverflow.com/questions/46641706/given-a-lat-long-find-the-nearest-location-based-on-a-json-list-of-lat-long?rq=1
R = 6371000 #radius of the Earth in m
def distance(lon1, lat1,  lon2, lat2):
    x = (-float(lon2) - -float(lon1)) * cos(0.5*(float(lat2)+float(lat1)))
    y = (float(lat2) - float(lat1))
    return R * sqrt( x*x + y*y )

# KnowledgeBase from Rasa documentation
class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("./actions/bank_data.json")
        knowledge_base.set_representation_function_of_object(
            "bank", lambda obj: obj["name"] + ", " + obj["google_location"] + " (" + obj["location"] + ")"
        )

        super().__init__(knowledge_base)
    
    # Overwrite how attributes are written
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
            if attribute_value is not None and object_name is not None:
                if attribute_name == 'opening_hours':
                    dispatcher.utter_message("Það er opið frá {} í {}.".format(attribute_value, object_name))
                    return
                if attribute_name == 'atm' and attribute_value is True:
                    dispatcher.utter_message("Það er hraðbanki í {}".format(object_name))
                else:
                    dispatcher.utter_message("Það er enginn hraðbanki í {}.".format(object_name))
            else:
                dispatcher.utter_message("Ég fann engar niðurstöður")

    # Overwrite utter_objects
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
                if object_type == 'bank':
                    repr_function = self.knowledge_base.get_representation_function_of_object(object_type)
                    if (len(objects)>1):
                        dispatcher.utter_message("Það eru nokkrir bankar")
                        for i, obj in enumerate(objects, 1):
                            dispatcher.utter_message("{}: {}".format(i, repr_function(obj)))
                    else:
                        dispatcher.utter_message("Það er einn")
                        for i, obj in enumerate(objects, 1):
                            dispatcher.utter_message("{}".format(repr_function(obj)))
            else:
                dispatcher.utter_message("Fyrirgefðu ég fann enga {}a á þessu svæði.".format(object_type))

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
            dispatcher.utter_message("Ég er ekkert fyndið í dag.")

        return []

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
            base = base.upper()
        if rate is not None:
            rate = rate.upper()

        if base is not None:
            r = requests.get(URL + '?base=' + base)
        else:
            r = requests.get(URL + '?base=ISK')
            
        try:
            response = r.text
            json_data = json.loads(response)
            rates = json.loads(response)['rates']
        except ValueError:
            dispatcher.utter_message("Fann ekki gjaldmiðil í gögnum")

        # Check which entities are in user query
        if rate is not None and base is not None and amount is not None:
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
            dispatcher.utter_message("Fannst ekki í gögnum")

        return []
        
class ActionSearchBanks(Action):
    def name(self) -> Text:
      
        return "action_query_search_banks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # use tracker to get last events metadata sent from front-end
        # metadata includes longitude and latitude of user if allowed
        state = tracker.current_state()
        last_events = state.get("events")
        most_recent = max(last_events, key=lambda e: e['timestamp'])
        longitude = most_recent["metadata"]["longitude"]
        latitude = most_recent["metadata"]["latitude"]
        
        #read out banks from our bank_data.json file
        banks = pd.read_json("./actions/bank_data.json", encoding = 'utf-8')['bank']

        #If latitude and longitude have been fetched the user has allowed for location
        if latitude is not None and longitude is not None:
            dispatcher.utter_template("utter_thanks_for_location", tracker)
            print("Þú ert hér: {} {}".format(latitude, longitude))
            sortedlist = sorted(banks, key = lambda d: distance(d['longitude'], d['latitude'], longitude, latitude))[0]
            dispatcher.utter_message("Næsti banki við þig er í:")
            dispatcher.utter_message("{}, {}, {}".format(sortedlist["name"], sortedlist["google_location"], sortedlist["location"]))
        else:
            dispatcher.utter_message("Þú hefur ekki leyft okkur að nálgast staðsetningu þína..")
       
        return []
            