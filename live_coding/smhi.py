# -*- coding: utf-8 -*-
"""Weather forecasting in Python"""

import json
import requests

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.dates as pltd

class SMHI:
    def __init__(self):

        self.url = "https://opendata-download-metfcst.smhi.se"
        self.api_template = "/api/category/{}/version/{}/geotype/point/lon/{}/lat/{}/data.json"

        self.category = "pmp3g"
        self.version = "2"
        self.longitude = "13.1"
        self.latitude = "55.7"

    def request_forecast(self):
        """Request data from SMHI"""

        api_string = self.api_template.format(self.category, self.version, self.longitude, self.latitude)

        smhi_info = requests.get(self.url + api_string)
        self.forecast = json.loads(smhi_info.text)

        self.__extract_param_names()
        self.__params_to_arrays()


    def __extract_param_names(self):

        names = {}

        for item in self.forecast["timeSeries"]:
            params = item["parameters"]
            for param in params:
                if not param["name"] in names:
                    names[param["name"]] = param["unit"]

        self.param_names = names

        return names

    def __extract_param(self, name):
        
        values = []

        for item in self.forecast["timeSeries"]:
            params = item["parameters"]
            for param in params:
                if param["name"] == name:
                    values.append([pltd.datestr2num(item["validTime"]),param["values"][0]])

        return np.array(values)

    def __params_to_arrays(self):

        self.values = {}

        for param in self.param_names:
            arr = self.__extract_param(param)
            self.values[param] = arr


if __name__ == "__main__":

    print("Weather forecasting in Python")

    smhi = SMHI()
    smhi.longitude = "13.2"
    smhi.request_forecast()

    plt.plot_date(smhi.values["t"][:,0], smhi.values["t"][:,1], xdate=True, fmt="r-")

    plt.show()