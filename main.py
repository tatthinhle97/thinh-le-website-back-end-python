from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.locations import states, cities
from routes.projects import sale_and_rental_listings
from routes import chat
from dotenv import load_dotenv

# This will be the main point of interaction to create all your API.
app = FastAPI()
load_dotenv()

origins = [
    'http://localhost:5173',
    'https://tatthinhle97.vercel.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(states.router)
app.include_router(cities.router)
app.include_router(sale_and_rental_listings.router)

@app.get('/')
async def root():
    return "Hi there"