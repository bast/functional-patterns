import time


def stand():
    print("Character is now standing.")

    def handle_input(key_input):
        if key_input == "DOWN_PRESS":
            return duck()
        elif key_input == "B":
            return jump()

    return handle_input


def duck():
    print("Character is now ducking.")
    start_time = time.time()

    def handle_input(key_input):
        if key_input == "DOWN_RELEASE":
            charge_duration = time.time() - start_time
            if charge_duration >= 2:
                print("Unleashing special attack!")
            else:
                print("Standing up without special attack.")
            return stand()

    return handle_input


def jump():
    print("Character is now jumping.")

    def handle_input(key_input):
        if key_input == "DOWN_PRESS":
            return dive()

    return handle_input


def dive():
    print("Character is now diving.")
    # diving has no transition defined, so it stays in this state
    return lambda key_input: dive


def character_state_machine():
    print("\nCharacter state machine initialized.")
    # initial state
    current_state = stand()

    def handle_input(key_input):
        nonlocal current_state
        print(f"Received input: {key_input}")
        current_state = current_state(key_input)

    return handle_input


if __name__ == "__main__":
    character = character_state_machine()
    character("DOWN_PRESS")
    time.sleep(3)
    character("DOWN_RELEASE")
    character("B")
    character("DOWN_PRESS")

    character = character_state_machine()
    character("DOWN_PRESS")
    time.sleep(1.5)
    character("DOWN_RELEASE")
    character("B")
