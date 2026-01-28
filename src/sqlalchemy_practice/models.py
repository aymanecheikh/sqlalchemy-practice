from sqlalchemy.orm import declarative_base

CONNECTION_STRING = (
  "mysql+mysqlconnector://aymane:aymane@localhost/sqlalchemy_practice"
)
Base = declarative_base()