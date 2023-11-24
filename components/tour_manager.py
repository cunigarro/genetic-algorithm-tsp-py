class TourManager:
    destination_cities = []

    @staticmethod
    def add_city(city):
        TourManager.destination_cities.append(city)

    @staticmethod
    def get_city(city_index):
        return TourManager.destination_cities[city_index]

    @staticmethod
    def number_of_cities():
        return len(TourManager.destination_cities)
