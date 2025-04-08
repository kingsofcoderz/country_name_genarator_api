from fastapi import FastAPI, Query
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

def generate_name(syllable_count: int, custom_ending: str = None):
    name = ''.join(random.choices(syllables, k=syllable_count)).capitalize()
    ending = custom_ending if custom_ending else random.choice(endings)
    return name + ending

def generate_country(syllable_count: int, custom_ending: str = None):
    name = generate_name(syllable_count, custom_ending)
    population = random.randint(1_000_000, 150_000_000)
    area_km2 = round(random.uniform(20_000, 2_500_000), 2)
    return {
        "name": name,
        "population": population,
        "area_km2": area_km2
    }

@app.get("/countryname")
def get_country_names(
    syllables: int = Query(None, ge=1, le=10),
    ending: str = None,
    count: int = Query(1, ge=1, le=100)
):
    syllable_count = syllables if syllables else random.randint(2, 4)
    if count == 1:
        return generate_country(syllable_count, ending)
    return [generate_country(syllable_count, ending) for _ in range(count)]
