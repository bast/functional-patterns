from abc import ABC, abstractmethod


# State Interface
class TrafficLightState(ABC):
    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def show(self):
        pass


# Concrete State: Red Light
class RedLightState(TrafficLightState):
    def next_state(self):
        return GreenLightState()

    def show(self):
        print("Red Light - STOP!")


# Concrete State: Green Light
class GreenLightState(TrafficLightState):
    def next_state(self):
        return YellowLightState()

    def show(self):
        print("Green Light - GO!")


# Concrete State: Yellow Light
class YellowLightState(TrafficLightState):
    def next_state(self):
        return RedLightState()

    def show(self):
        print("Yellow Light - SLOW DOWN!")


# Context: Traffic Light
class TrafficLight:
    def __init__(self):
        self.state = RedLightState()

    def change_state(self):
        self.state = self.state.next_state()

    def show_light(self):
        self.state.show()


if __name__ == "__main__":
    traffic_light = TrafficLight()

    for _ in range(6):
        traffic_light.show_light()
        traffic_light.change_state()
