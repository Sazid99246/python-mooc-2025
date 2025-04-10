class WeatherStation:
    def __init__(self, name):
        self._name = name
        self._observations = []

    def add_observation(self, observation: str):
        self._observations.append(observation)

    def latest_observation(self):
        return self._observations[-1] if len(self._observations) > 0 else ""

    def number_of_observations(self):
        return len(self._observations)

    def __str__(self):
        return f"{self._name}, {self.number_of_observations()} observations"


if __name__ == "__main__":
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
