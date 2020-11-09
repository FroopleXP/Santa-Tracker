import time
import math
import json
from datetime import datetime

class SantaLocation:

    def __init__(self, dest, array, index):

        self.id = dest["id"]
        self.arrival = dest["arrival"]
        self.departure = dest["departure"]
        self.presentsDelivered = dest["presentsDelivered"]
        self.population = dest["population"]
        self.city = dest["city"]
        self.region = dest["region"]
        self.location = dest["location"]
        self.details = dest["details"]

        self.__index = index
        self.__array = array

    def prev(self):
        return self.__array[0 if self.__index - 1 < 0 else self.__index - 1]

    def next(self):
        return self.__array[self.__index + 1] or self.__array[len(self.__array) - 1]

class SantaTracker:

    def __init__(self, offset=0):
        self.__destinations = self.__map_json_to_destinations(self.__load_destinations())
        self.__TIME_OFFSET = offset
        self.__PRESENTS_OVER_WATER = .3
        self.__PRESENTS_IN_CITY = 1 - self.__PRESENTS_OVER_WATER

    def __map_json_to_destinations(_, json):
        arr = []
        for idx, dest in enumerate(json["destinations"]):
            arr.append(SantaLocation(dest, arr, idx))
        return arr

    def __load_destinations(self):
        with open("data/tracking_data.json", "r") as f:
            return json.load(f)


    def __findDestination(self, timestamp):

        if (not len(self.__destinations)):
            return None

        # If it's not xmas eve. he's not set off set
        if (self.__destinations[0].departure > timestamp):
            return self.__destinations[0]

        # Get the current destination
        for idx, dest in enumerate(self.__destinations):
            if (timestamp < dest.arrival):
                return self.__destinations[idx - 1]

    def get_adj_time(self):
            current_year = datetime.now().year
            time_takeoff_this_year = int(datetime.strptime("24/12/{} 10:00:00".format(current_year), "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
            time_data_starts = int(datetime.strptime("24/12/2019 10:00:00", "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
            time_diff = int(time_takeoff_this_year - time_data_starts)

            return (int(time.time() * 1000) - time_diff) + self.__TIME_OFFSET

    def __calculatePresentsDelivered(self, now, prev, stopover, next):
        
        if (not stopover):
            elapsed = now - prev.departure
            duration = next.arrival - prev.departure
            delivering = next.presentsDelivered - prev.presentsDelivered
            delivering *= self.__PRESENTS_OVER_WATER

            return math.floor(prev.presentsDelivered + delivering * elapsed / duration)

        elapsed = now - stopover.arrival                                    # How long we've been at the stop for
        duration = (stopover.departure - stopover.arrival) or 1e-10         # How long we're at the stop for - Note: As we can't divide by 0, we default to 1e-10 (0.00000000001) if stop delta is 0
        delivering = stopover.presentsDelivered - prev.presentsDelivered    # Total presents to deliver before we take off

        return math.floor(prev.presentsDelivered + (delivering * self.__PRESENTS_OVER_WATER) + (delivering * self.__PRESENTS_IN_CITY) * elapsed / duration)
        

    def getCurrentLocation(self):

        now = self.get_adj_time() # Note: mapping to 13 unix timestamp, the same as the default Date() method in JS
        dest = self.__findDestination(now)
        next = dest.next()

        # Check if Santa is at a location or in transit
        if (now < dest.departure):
            # At location
            return { 
                "position": dest.location,
                "presentsDelivered": self.__calculatePresentsDelivered(now, dest.prev(), dest, next),
                "prev": dest.prev(),
                "next": next,
                "stopover": dest
            }

        # In Transit
        return { 
            "position": dest.location,
            "presentsDelivered": self.__calculatePresentsDelivered(now, dest, None, next),
            "prev": dest.prev(),
            "next": next,
            "stopover": None
        }
        
        

