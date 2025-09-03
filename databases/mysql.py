import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

host = os.getenv("DATABASE_HOST")
port = os.getenv("DATABASE_PORT")
user = os.getenv("DATABASE_USER")
password = os.getenv("DATABASE_PASSWORD")
database_name = os.getenv("DATABASE_NAME")

# https://docs.sqlalchemy.org/en/20/dialects/mysql.html#module-sqlalchemy.dialects.mysql.pymysql
# https://pymysql.readthedocs.io/en/latest/user/installation.html
DATABASE_URL = f'''mysql+pymysql://{user}:{password}@{host}:{port}/{database_name}'''

database_engine = create_engine(DATABASE_URL)
# The sessionmaker factory generates new Session objects when called, creating them given the configurational arguments
# established here.
database_session_factory = sessionmaker(database_engine)

# For dependency injection
def get_db_session():
    db_session = database_session_factory()
    try:
        # Instead of using a return statement, the yield keyword pauses the function's execution and hands over
        # the db object to the code that called it. The function's state is preserved, and it waits for further
        # instructions.
        yield db_session
    finally:
        # This line closes the database session. Closing the session releases the connection back to the connection
        # pool, freeing up resources.
        db_session.close()