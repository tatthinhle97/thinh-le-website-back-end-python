from fastapi import FastAPI
from locations import states, cities
from projects import sale_and_rental_listings

# This will be the main point of interaction to create all your API.
app = FastAPI()
app.include_router(states.router)
app.include_router(cities.router)
app.include_router(sale_and_rental_listings.router)

@app.get('/')
async def root():
    return {'message': 'Hello World'}