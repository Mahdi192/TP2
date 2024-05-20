import csv
import json
from math import radians, sin, cos, sqrt, atan2

class donneesgeo:
    def __init__(self, ville, pays, latitude, longitude):
        self.ville = ville
        self.pays = pays
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    def __str__(self):
        return f"{self.ville}, {self.pays}, {self.latitude}, {self.longitude}"


