import datetime
from enum import Enum


class Plant:
    id = 0
    def __init__(self, name, water_level, sun_level):
        self.id = self.generate_id()
        self.name = name
        self.water_level = water_level
        self.sun_level = sun_level

    @classmethod
    def generate_id(cls):
        id = cls.id + 1
        cls.id += 1
        return id



class Alerts(Enum):
    WATER = "Alert_water"
    SUN = "Alert_sun"


class Event:
    created_events = []

    def __init__(self, type_event, plant: Plant):
        self.event = dict()
        self.event["type_event"] = type_event
        self.event["producer_type"] = type(plant).__name__
        self.event["producer_id"] = plant.id
        self.event["time_created"] = str(datetime.datetime.now())
        Event.created_events.append(self.event)


rose = Plant("Rose", 0, 0)
sunflower = Plant("Sunflower", 0, 0)
Event(Alerts.WATER,  rose)
Event(Alerts.SUN,  sunflower)

print(Event.created_events)
