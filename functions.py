def distance_from_zero(num):
  if type(num) == int or type(num) == float:
    return abs(num)
  else:
    return "nope"

print distance_from_zero('a')
