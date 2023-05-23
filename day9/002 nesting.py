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

def add_new_country(country,times,cities):
    new_add={"country" : country,"visits" : times,"cities" : cities}
    travel_log.append(new_add)


add_new_country(country="Russia", times=2, cities= ["Moscow", "Saint Petersburg"])
print(travel_log)
