from collections import defaultdict
from logger import get_logger
from exceptions import GardenError, WaterError

logger = get_logger("EventBus")


class EventBus:
    def __init__(self):
        # Dictionary: { "EVENT_TYPE": [function1, function2] }
        self._subscribers = defaultdict(list)

    def subscribe(self, event_type: str, handler: callable):
        self._subscribers[event_type].append(handler)
        logger.info(f"Registered {handler.__name__} for {event_type}")

    def publish(self, event: dict):
        e_type = event.get("type")
        handlers = self._subscribers.get(e_type, [])

        if not handlers:
            logger.warning(f"No one is listening for {e_type}")
            return
        for handler in handlers:
            handler()


class WateringSystem:
    tank_level = 0

    def water_plant(cls):
        if cls.tank_level < 20:
            raise WaterError("Not enough water")
        print("plant received water ")

class Garden:
    water_tank = WateringSystem
    water_tank.tank_level = 10

    def __init__(self, name: str, bus: EventBus, water_tank=water_tank) -> None:
        self.name = name
        self.bus = bus
        self.bus.subscribe("WATER_REQUEST", water_tank.water_plant)



class Plant:
    def __init__(self, name, bus: EventBus):
        self.name = name
        self.bus = bus

    def get_thirsty(self):
        logger.info(f"{self.name} is dry!")
        # The plant "shouts" into the bus
        self.bus.publish({
            "type": "WATER_REQUEST",
            "name": self.name
        })


if __name__ == "__main__":
    bus = EventBus()
    mygarden = Garden("Royal Garden", bus)
    rose = Plant("Rose", bus)
    rose.get_thirsty()
