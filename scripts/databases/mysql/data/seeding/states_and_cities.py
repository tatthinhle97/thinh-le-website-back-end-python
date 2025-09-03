import pandas as pd
from sqlalchemy import inspect
from databases.mysql import database_engine
from models.locations import CityModel, StateModel

# Read US cities data
us_cities_df = pd.read_csv('uscities.csv')


# Trim columns
us_cities_df['state_id'] = us_cities_df['state_id'].str.strip()
us_cities_df['state_name'] = us_cities_df['state_name'].str.strip()
us_cities_df['county_name'] = us_cities_df['county_name'].str.strip()
us_cities_df['city_ascii'] = us_cities_df['city_ascii'].str.strip()

# Extract into state_df
state_df = us_cities_df[['state_id', 'state_name']]
#   Rename columns
state_df = state_df.rename(columns={"state_id": "id", "state_name": "name"})
#   Drop duplicates and sort
state_df = state_df.drop_duplicates().sort_values('name')
#   Drop rows which are not states
state_df = state_df[(
        (state_df['name'] != 'Puerto Rico') &
        (state_df['name'] != 'District of Columbia')
)]


# Extract into city_df
city_df = us_cities_df[['state_id', 'county_name', 'city_ascii']]
#   Rename columns
city_df = city_df.rename(columns={
    "county_name": "county",
    "city_ascii": "city"
})
#   Drop duplicates and sort
city_df = (city_df
    .drop_duplicates(subset=['state_id', 'county', 'city'])
    .sort_values(by=['state_id', 'city']))
#   Filter cities in valid states
city_df = city_df[city_df['state_id'].isin(state_df['id'])]


# Create an inspector
inspector = inspect(database_engine)


# Drop if cities and states tables exist
if (CityModel.__tablename__ in inspector.get_table_names()
        or StateModel.__tablename__ in inspector.get_table_names()):
    CityModel.__table__.drop(database_engine, checkfirst=True)
    StateModel.__table__.drop(database_engine, checkfirst=True)

# Create tables
StateModel.__table__.create(database_engine, checkfirst=True)
CityModel.__table__.create(database_engine, checkfirst=True)

# Import states to database
try:
    state_df.to_sql(StateModel.__tablename__,
                    con=database_engine,
                    # Don't replace table, use append instead
                    if_exists="append",
                    index=False)
    print(f'Successfully inserted data into the states table')
except Exception as exception:
    print(f'Failed to insert data into the states table. Error: {exception}')

# Import cities to database
try:
    city_df.to_sql(CityModel.__tablename__,
                    con=database_engine,
                    # Don't replace table, use append instead
                    if_exists="append",
                    index=False)
    print(f'Successfully inserted data into the cities table')
except Exception as exception:
    print(f'Failed to insert data into the states table. Error: {exception}')



