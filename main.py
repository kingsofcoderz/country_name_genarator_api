from fastapi import FastAPI
import random

app = FastAPI()

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
              "p", "q", "r", "s", "t", "v", "w", "x", "y", "z", "th", "zh", "ph", "ch"]
vowels = ["a", "e", "i", "o", "u", "ae", "ai", "ou", "ia", "ea"]

def random_syllable():
    return random.choice(consonants).capitalize() + random.choice(vowels)

def generate_country_name():
    syllables = random.randint(2, 4)
    name = ''.join(random_syllable() for _ in range(syllables)) + "ia"
    return name

@app.get("/countryname")
def get_country_name():
    return {"name": generate_country_name()}
