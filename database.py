from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# MySQL connection URL using mysql-connector-python
DATABASE_URL = "mysql+mysqlconnector://root:ragasapa@localhost:3306/sakthi"

# Create engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)