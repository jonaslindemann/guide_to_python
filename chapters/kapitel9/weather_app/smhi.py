# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:37:54 2018

@author: Jonas Lindemann
"""

import json
import requests

import numpy as np
import matplotlib.pyplot as plt

class SMHI():
    """Class for extracting a weather forecast"""
    def __init__(self):
        """Class constructor"""

        self.url = "https://opendata-download-metfcst.smhi.se"
        self.api_template = "/api/category/{}/version/{}/geotype/point/lon/{}/lat/{}/data.json"
        self.category = "pmp3g"
        self.version = "2"
        self.longitude = "16"
        self.latitude = "58"
        self.request_forecast()

    def request_forecast(self):
        """Request data from SMHI"""

        api_string = self.api_template.format(self.category,
                                              self.version,
                                              self.longitude,
                                              self.latitude)

        smhi_info = requests.get(self.url + api_string)

        self.forecast = json.loads(smhi_info.text)

    def extract_param_names(self):
        """Return a list with available param_names"""

        names = {}

        for item in self.forecast["timeSeries"]:
            params = item["parameters"]
            for param in params:
                if not param["name"] in names:
                    names[param["name"]] = param["unit"]

        return names

    def extract_param(self, name):
        """Extract specific values from data"""

        values = []

        for item in self.forecast["timeSeries"]:
            params = item["parameters"]
            for param in params:
                if param["name"] == name:
                    values.append([item["validTime"], param["values"][0]])

        return np.asanyarray(values)
    
if __name__ == '__main__':

    smhi = SMHI()
    params = smhi.extract_param_names()
    values = smhi.extract_param("r")

    print(params)
    print(values)

    plt.plot_date(values[:, 0], values[:, 1], xdate=True, fmt="r-")
    