from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DB_URL")


engine = create_engine(db_url)

sessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally:    
         db.close()

