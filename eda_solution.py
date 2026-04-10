from collections import defaultdict
from enum import Enum


# ----- Step 1: Define events -----
class Alert(Enum):
    WATER = 20
    SUN = 10


# Standardized Event object
class Event:
    def __init__(self, name_alert: str, source, payload: dict):
        self.name_alert = name_alert
        self.source = source      # The producer, e.g., Plant
        self.payload = payload    # All data subscribers might need


# ----- Step 2: Define the EventBus -----
class EventBus:
    def __init__(self):
        self.subscribers = defaultdict(list)

    def subscribe(self, event_type: str, handler):
        self.subscribers[event_type].append(handler)

    def publish(self, event: Event):
        # Always safe to iterate, even if no subscribers
        for handler in self.subscribers.get(event.name_alert, []):
            handler(event)


# ----- Step 3: Define autonomous services (subscribers) -----
class WaterSystem:
    def add_water(self, event: Event):
        plant = event.source
        plant.level_water += 50
        print(f"[WaterSystem] Watered {plant.name}."
              f"New level: {plant.level_water}")


class LightSystem:
    def add_sun(self, event: Event):
        plant = event.source
        plant.level_light += 10
        print(f"[LightSystem] Sunlight added to {plant.name}."
              f"New level: {plant.level_light}")


# ----- Step 4: Define the Plant (event producer) -----
class Plant:
    def __init__(self, name: str, bus: EventBus, level_water=100, level_light=100):
        self.name = name
        self.level_water = level_water
        self.level_light = level_light
        self.bus = bus

    def consume_resources(self):
        self.level_water -= 20
        self.level_light -= 20
        print(f"[Plant] {self.name} consumed resources."
              f"Water: {self.level_water}, Light: {self.level_light}")

    def check_needs(self):
        # Check water
        if self.level_water < Alert.WATER.value:
            event = Event(name_alert="WATER", source=self,
                          payload={"current_water": self.level_water})
            self.bus.publish(event)

        # Check sunlight
        if self.level_light < Alert.SUN.value:
            event = Event(name_alert="SUN", source=self,
                          payload={"current_light": self.level_light})
            print("event sunlight", event)
            self.bus.publish(event)


# ----- Step 5: Setup and wiring -----
bus = EventBus()
water_system = WaterSystem()
light_system = LightSystem()

# Subscribe systems to events
bus.subscribe("WATER", water_system.add_water)
bus.subscribe("SUN", light_system.add_sun)

print("subscribers ", bus.subscribers)

# Create plants
rose = Plant("Rose", bus, level_water=15, level_light=15)
tulip = Plant("Tulip", bus, level_water=50, level_light=5)

# Simulate plant lifecycle
plants = [rose, tulip]
for plant in plants:
    plant.consume_resources()
    plant.check_needs()
