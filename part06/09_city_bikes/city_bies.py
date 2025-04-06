import math


def get_station_data(filename: str):
    distance = {}
    with open(filename) as file:
        next(file)
        for line in file:
            line = line.strip()
            line_as_list = line.split(';')
            if len(line_as_list) >= 4:
                lat = float(line_as_list[0])
                lon = float(line_as_list[1])
                name = line_as_list[3]
                distance[name] = (lat, lon)
    return distance


def distance(stations: dict, station1: str, station2: str):
    longitude1 = 0
    latitude1 = 0
    longitude2 = 0
    latitude2 = 0
    for station in stations:
        if station == station1:
            longitude1 = stations[station][0]
            latitude1 = stations[station][1]
        if station == station2:
            longitude2 = stations[station][0]
            latitude2 = stations[station][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km


def greatest_distance_from_one_station(stations: dict, stations_list: list, station: str):
    start_index = stations_list.index(station)+1
    compare_list = stations_list[start_index:]
    greatest_tuple = None
    greatest = 0
    for compare in compare_list:
        d = distance(stations, station, compare)
        if d > greatest:
            greatest_tuple = (station, compare, d)
            greatest = d
    return greatest_tuple


def greatest_distance(stations: dict):
    stations_list = []
    for key, value in stations.items():
        stations_list.append(key)

    greatest_tuple = None
    greatest = 0
    for index, station in enumerate(stations_list):
        if index < len(stations_list)-1:
            stations_distance = greatest_distance_from_one_station(
                stations, stations_list, station)
            station1, station2, distance = stations_distance
            if distance > greatest:
                greatest_tuple = stations_distance
                greatest = distance

    return greatest_tuple
