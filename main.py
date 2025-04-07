from fastapi import FastAPI, Query
import random

app = FastAPI()

# List of premade syllables to build names from
SYLLABLES = [
    "ka", "lo", "va", "ra", "ze", "to", "na", "mi", "shi", "ko", 
    "li", "ga", "ba", "di", "tu", "ne", "xo", "qui", "jo", "fi"
]

@app.get("/countryname")
def get_country_name(syllables: int = Query(3, ge=1, le=5)):
    name = ''.join(random.choice(SYLLABLES).capitalize() for _ in range(syllables)) + "ia"
    return {"name": name}
