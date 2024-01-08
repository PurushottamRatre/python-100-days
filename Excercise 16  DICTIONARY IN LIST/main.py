country = input("Which country you visited?  ")
visits = int(input("How many times you visited? "))
list_of_cities = eval(input("Which cities you visited there? ")) # create list from formatted string
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]


def add_new_country(name, times_visited, cities_visited):
    new_country = {"country": name, "visits": times_visited, "cities": cities_visited}
    travel_log.append(new_country)


add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")