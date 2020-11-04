import json
import time
from datetime import datetime

class SantaTracker:

    def __init__(self):
        self.__tracking_data = self.__load_data()


    def __load_data(self):
        with open("data/tracking_data.json", "r") as json_file:
            return json.load(json_file)

    def __get_index_from_id(self, id):
        for idx, dst in enumerate(self.__tracking_data["destinations"]):
            if (dst["id"] == id):
                return idx + 1
        return None

    def __get_adj_time(self):
        current_year = datetime.now().year
        time_takeoff_this_year = int(datetime.strptime("24/12/{} 10:00:00".format(current_year), "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
        time_data_starts = int(datetime.strptime("24/12/2019 10:00:00", "%d/%m/%Y %H:%M:%S").timestamp() * 1000)
        time_diff = int(time_takeoff_this_year - time_data_starts)
        return int(time.time() * 1000) - time_diff

    def getcurrentlocation(self, offset=0):

        time = self.__get_adj_time() + offset
        latest_dst = self.__tracking_data["destinations"][0]

        for destination in self.__tracking_data["destinations"]:
            if (time >= destination["arrival"]):
                latest_dst = destination

        return latest_dst

    def getcurrentstatus(self, offset=0):

        time = self.__get_adj_time() + offset
        latest_status = self.__tracking_data["stream"][0]

        for status in self.__tracking_data["stream"]:
            if (time >= status["timestamp"]):
                if ("status" in status):
                    latest_status = status

        return latest_status

    def getstopsfrom(self, id="edinburgh", time_offset=0):

        target = self.__get_index_from_id(id)
        
        # TODO: This ideally needs to throw an error if the target does not exist
        if (target == None):
            target = 0

        curr = self.__get_index_from_id(self.getcurrentlocation(time_offset)["id"])
        return int(target-curr)

