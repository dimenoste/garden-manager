from enum import Enum

# class syntax
class Alert(Enum):
    WATER_REQUEST = "WATER_REQUEST"
    SUN_REQUEST = "WATER_REQUEST"
    READY_HARVEST = "READY_HARVEST"


class GardenError(Exception):
    pass

class WaterError(GardenError):
    def __init__(self, msg):
        super().__init__(f"WaterError {msg}")
