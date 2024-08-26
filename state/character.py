import time
from abc import ABC, abstractmethod


# abstract base class for states
class CharacterState(ABC):
    @abstractmethod
    def handle_input(self, character, key_input):
        pass

    @abstractmethod
    def enter_state(self, character):
        pass


class StandingState(CharacterState):
    def handle_input(self, character, key_input):
        if key_input == "DOWN_PRESS":
            character.change_state(DuckingState())
        elif key_input == "B":
            character.change_state(JumpingState())

    def enter_state(self, character):
        print("Character is now standing.")


# ducking state with charge mechanic
class DuckingState(CharacterState):
    def __init__(self):
        self.start_time = None

    def handle_input(self, character, key_input):
        if key_input == "DOWN_RELEASE":
            charge_duration = time.time() - self.start_time
            # assume 2 seconds is required to charge the special attack
            if charge_duration >= 2:
                print("Unleashing special attack!")
            else:
                print("Standing up without special attack.")
            character.change_state(StandingState())

    def enter_state(self, character):
        print("Character is now ducking.")
        self.start_time = time.time()


class JumpingState(CharacterState):
    def handle_input(self, character, key_input):
        if key_input == "DOWN_PRESS":
            character.change_state(DivingState())

    def enter_state(self, character):
        print("Character is now jumping.")


class DivingState(CharacterState):
    def handle_input(self, character, key_input):
        pass  # No transitions defined from Diving

    def enter_state(self, character):
        print("Character is now diving.")


class Character:
    def __init__(self):
        self.state = StandingState()
        self.state.enter_state(self)

    def change_state(self, new_state):
        self.state = new_state
        self.state.enter_state(self)

    def handle_input(self, key_input):
        print(f"Received input: {key_input}")
        self.state.handle_input(self, key_input)


if __name__ == "__main__":
    character = Character()
    character.handle_input("DOWN_PRESS")
    time.sleep(3)
    character.handle_input("DOWN_RELEASE")
    character.handle_input("B")
    character.handle_input("DOWN_PRESS")

    character = Character()
    character.handle_input("DOWN_PRESS")
    time.sleep(1.5)
    character.handle_input("DOWN_RELEASE")
    character.handle_input("B")
