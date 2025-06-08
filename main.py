from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from locations import states, cities
from projects import sale_and_rental_listings
import os
from dotenv import load_dotenv



# This will be the main point of interaction to create all your API.
app = FastAPI()
load_dotenv()

origins = [
    os.getenv("FRONT_END_ORIGIN")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(states.router)
app.include_router(cities.router)
app.include_router(sale_and_rental_listings.router)

@app.get('/')
async def root():
    return "Hi there!"