import datetime
from enum import Enum


class Plant:
    id = 0

    def __init__(self, name, water_level, sun_level) -> None:
        self.id = self.generate_id()
        self.name = name
        self.water_level = water_level
        self.sun_level = sun_level

    @classmethod
    def generate_id(cls) -> int:
        id = cls.id + 1
        cls.id += 1
        return id


class Alerts(Enum):
    WATER = "Alert_water"
    SUN = "Alert_sun"


class WateringSystem:

    def add_water(plant: Plant):
        if plant.water_level <= 100:
            plant.water_level += 20


class SunSystem():
    def add_sun(plant: Plant):
        if plant.sun_level <= 100:
            plant.sun_level += 20


class Event:
    created_events = []

    def __init__(self) -> None:
        self.event = dict()
        self.handlers = dict()

    def subscribe(self, type_event: str,
                  handler: callable) -> None:
        print(type_event)
        if type_event not in self.handlers:
            self.handlers[type_event] = set()
        self.handlers[type_event].add(handler)

    def publish(self, type_event: str, plant: Plant) -> None:
        self.event["type_event"] = type_event
        self.event["producer_type"] = type(plant).__name__
        self.event["producer_id"] = plant.id
        self.event["time_created"] = str(datetime.datetime.now())
        self.update_events_log(self.event)

        for handler in self.handlers[type_event]:
            handler(plant)

    @classmethod
    def update_events_log(cls, event) -> None:
        cls.created_events.append(event)




rose = Plant("Rose", 0, 0)
sunflower = Plant("Sunflower", 0, 0)

event = Event()
print("Alerts.WATER", Alerts.WATER)
event.subscribe(Alerts.WATER, WateringSystem.add_water)
event.subscribe(Alerts.SUN, SunSystem.add_sun)

print(rose.water_level)

event.publish(Alerts.WATER, rose)
event.publish(Alerts.SUN, sunflower)

print(rose.water_level)
print(Event.created_events)
