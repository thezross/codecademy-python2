"""Program is going to calcualte the cost
of my vacation"""

def hotel_cost(nights):
	return 140 * nights

# function provides cost given city
def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

  def rental_car_cost(days):
    new = days * 40
    if days >= 7:
      new = new - 50
    elif days >= 3 and days <= 6:
      new = new - 20
    return new

  def trip_cost(city, days, spending_money):
    return hotel_cost(days - 1) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

  print trip_cost("Los Angeles", 5, 600)
  
