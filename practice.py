def median(numbers):
  slist = sorted(numbers)
  nr = len(numbers)
  factor = 1 - nr % 2

  return (float(slist[ int(nr/2 - factor)]) + slist[int(nr/2)])/2

print median([4,5,5,4])
