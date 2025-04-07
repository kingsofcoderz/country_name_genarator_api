from fastapi import FastAPI, Query
import random

app = FastAPI()

SYLLABLES = [
    "ka", "lo", "va", "ra", "ze", "to", "na", "mi", "shi", "ko", 
    "li", "ga", "ba", "di", "tu", "ne", "xo", "qui", "jo", "fi"
]

ENDINGS = ["ia", "an", "ar", "stan", "land", "on", "os", "ora", "eria", "vania"]

@app.get("/countryname")
def get_country_name(
    syllables: int = Query(3, ge=1, le=5),
    ending: str = Query(None)
):
    name_body = ''.join(random.choice(SYLLABLES) for _ in range(syllables))
    name_ending = ending if ending else random.choice(ENDINGS)
    full_name = (name_body + name_ending).capitalize()
    return {"name": full_name}
