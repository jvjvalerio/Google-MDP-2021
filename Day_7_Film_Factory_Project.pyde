import random
i = 0

title = ["The return of ", "The wonderful world of ", "The harrowing tales of ", "A day with ", "Getting to know "]
characters = ["Rocky: ", "Gandalf: ", "Mario: ", "Godzilla: ", "Jack Sparrow: "]
tagLines = ["From the moment they met, it was murder", "When you deal a fast shuffle, love is in the cards", "They were 7...and they fought like 700.", "The story of a man who was too proud to run.", "Who you gonna call?"]

for movieTitle in title:
        for movieCharacter in characters:
            for movieTags in tagLines:
                if i < 10:
                 print(random.choice(title) + random.choice(characters) + random.choice(tagLines)) 
                 i += 1
