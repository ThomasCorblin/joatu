from math import pi, acos, cos, sin
from hubs.models import HubGeolocation
from decimal import Decimal

def distance_calculation(offer, hub): 
    project_lat_conv = offer.lat * Decimal(pi) / 180
    project_lng_conv = offer.lng * Decimal(pi) / 180
    hub_lat_conv = hub.lat * Decimal(pi) /180
    hub_lng_conv = hub.lng * Decimal(pi) / 180
    R = 6371
    d = R * acos(cos(project_lat_conv)*cos(hub_lat_conv)*cos(hub_lng_conv-project_lng_conv)+sin(project_lat_conv)*sin(hub_lat_conv))
    distance_km = round(Decimal(d),3)
    return distance_km