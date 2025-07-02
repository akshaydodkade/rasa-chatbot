from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionBookMeeting(Action):
  def name(self) -> str:
    return "action_book_meeting"
  
  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
    time = tracker.get_slot("time")
    dispatcher.utter_message(response="utter_confirm_booking", time=time)
    return [SlotSet("time", time)]