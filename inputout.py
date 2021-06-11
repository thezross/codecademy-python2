with open("text.txt", "w") as textfile:
  textfile.write("Success!")

if textfile.close == False:
  textfile.closed

print textfile.closed
