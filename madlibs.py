"""
This program generates passages that are generated in mad-lib format
Author: Zach
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."


name = raw_input("Enter a name:  ")
adj1 = raw_input("Enter an adjective:  ")
adj2 = raw_input("Enter an adjective:  ")
adj3 = raw_input("Enter an adjective:  ")
verb = raw_input("Enter a verb:  ")
noun1 = raw_input("Enter a noun:  ")
noun2 = raw_input("Enter a noun:  ")
aanimal = raw_input("Enter an animal:  ")
afood = raw_input("Enter a food:  ")
afruit = raw_input("Enter a fruit:  ")
asuperhero = raw_input("Enter a superhero:  ")
acountry = raw_input("Enter a county:  ")
adessert = raw_input("Enter a dessert:  ")
ayear = raw_input("Enter a year:  ")

print STORY % (name, adj1, adj2, aanimal, afood, verb, noun1, afruit, adj3, name, asuperhero, name,acountry, name, adessert, name, ayear, noun2)
