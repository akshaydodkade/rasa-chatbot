from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionBookMeeting(Action):
  def name(self) -> str:
    return "action_book_meeting"

  def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
    time = tracker.get_slot("time")
    if time:
      dispatcher.utter_message(response="utter_confirm_booking", time=time)
    else:
      dispatcher.utter_message(text="Sorry, I couldn’t understand the time. Could you clarify?")
    return [SlotSet("time", time)]