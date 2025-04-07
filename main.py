from fastapi import FastAPI
from fastapi.responses import JSONResponse
import random

app = FastAPI()

syllables = [
    "xa", "zu", "lo", "ka", "re", "tu", "ne", "ri", "sha", "vo",
    "mi", "ga", "so", "ni", "za", "fa", "lu", "po", "chi", "dra",
    "ba", "qui", "jo", "te", "la", "vi", "mo", "no", "gu", "sa",
    "je", "ro", "ki", "do", "ya", "ce", "wi", "nu", "hi", "be",
    "pla", "sti", "dro", "bro", "gha", "kra", "zhe", "blo", "tra", "fle"
]

endings = [
    "ia", "ania", "ara", "eria", "oria", "esia", "alia", "enia", "una", "asha",
    "oriah", "ennia", "quon", "estia", "ystan", "stan", "iq", "aq", "ur", "oth",
    "val", "ox", "myr", "ador", "ek", "dan", "dar", "alon", "und", "tara", "moor",
    "lund", "mar", "ith", "grad", "hive", "mere", "vax", "bira", "zhan"
]

def generate_country_name():
    name = ''.join(random.choices(syllables, k=3)).capitalize()
    return name + random.choice(endings)

def generate_population():
    return f"{random.randint(1_000_000, 150_000_000):,}"

def generate_area():
    return f"{random.randint(20_000, 3_000_000):,}"

@app.get("/countryname")
def get_country():
    return JSONResponse({
        "name": generate_country_name(),
        "population": generate_population(),
        "area_km2": generate_area()
    })
