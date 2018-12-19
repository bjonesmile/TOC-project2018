from transitions.extensions import GraphMachine

from utils import send_text_message

import random

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )
    def choose_ironclad(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'choose ironclad'
        return False

    def choose_silent(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'choose silent'
        return False

    def choose_defect(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'choose defect'
        return False

    def on_enter_ironclad(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "I've chosen ironclad")
        self.go_back()

    def on_enter_silent(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "I've chosen silent")
        self.go_back()

    def on_enter_defect(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "I've chosen defect")
        self.go_back()

    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False

    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state3'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        a=random.randint(1,10)
        responese = send_text_message(sender_id, "damage:")
        responese = send_text_message(sender_id, a)
        print(a)
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')

    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state3")
        self.go_back()

    def on_exit_state3(self):
        print('Leaving state3')

    def is_going_to_monster1(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go slay the spire'
        return False

    def on_enter_monster1(self, event):
        print("I'm entering floor1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor1")
    
    def is_going_to_monster2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor2'
        return False

    def on_enter_monster2(self, event):
        print("I'm entering floor2")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor2")

    def is_going_to_elite(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor3'
        return False

    def on_enter_elite(self, event):
        print("I'm entering floor3")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor3")

    def is_going_to_monster3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor4'
        return False

    def on_enter_monster3(self, event):
        print("I'm entering floor4")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor4")

    def is_going_to_monster4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor5'
        return False

    def on_enter_monster4(self, event):
        print("I'm entering floor5")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor5")

    def is_going_to_finalboss(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor6'
        return False

    def on_enter_finalboss(self, event):
        print("I'm entering floor6")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor6")
    
    def is_going_to_finalboss(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor6'
        return False

    def on_enter_finalboss(self, event):
        print("I'm entering floor7")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "Here is finalboss")

    def is_going_to_theend(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to floor7'
        return False

    def on_enter_theend(self, event):
        print("I'm entering floor7")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering floor7.It's not end. Time to reborn.")
        self.go_back()

