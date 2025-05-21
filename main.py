from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from locations import states, cities
from projects import sale_and_rental_listings

# This will be the main point of interaction to create all your API.
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://tatthinhle.vercel.app"
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