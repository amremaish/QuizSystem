from datetime import datetime
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0


def get_distance(lat1, lon1, lat2, lon2):
    radians_lat1 = radians(lat1)
    radians_lon1 = radians(lon1)
    radians_lat2 = radians(lat2)
    radians_lon2 = radians(lon2)

    dlon = radians_lon2 - radians_lon1
    dlat = radians_lat2 - radians_lat1

    a = sin(dlat / 2) ** 2 + cos(radians_lat1) * cos(radians_lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance


def is_date_between_today(from_date, to_date):
    return str(from_date) < datetime.today().strftime("%Y-%m-%d") < str(to_date)


def is_time_between_today(from_time, to_time):
    return str(from_time) < datetime.now().strftime("%H:%M:%S") < str(to_time)
